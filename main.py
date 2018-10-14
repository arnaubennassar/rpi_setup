import os
import getpass
import helper_functions as hf
import module.spotify as spotify
import module.transmission as transmission
import module.sick_rage as sick_rage
import module.radarr as radarr
import module.couchpotato as couchpotato
import module.next_cloud as next_cloud
import module.zsh as zsh
import config as c

transmission_installed = False
user_name = getpass.getuser()
final_output = ''

#SETUP DIRECTORIES
os.system("mkdir "+c.download_dir)
os.system("mkdir "+c.series_dir)
os.system("mkdir "+c.movies_dir)
#INSTALL MANDATORY STUFF
os.system("sudo apt-get update")
if os.system("git --version") != 0:
    print("INSTALLING git.")
    os.system("sudo apt-get install git -y")

if c.install_spotify == 'yes':
    print("INSTALLING SPOTIFY!")
    final_output += spotify.install(c.spotify_name)

if c.install_flexget == 'yes':
    print("INSTALLING FLEXGET!")
    if not transmission_installed:
        final_output += transmission.install(c.disk_name, c.transmission_user, c.transmission_pass, c.download_dir)
        transmission_installed = True
    os.system("mkdir ~/flexget")
    os.system("cp /home/osmc/Documents/rpi_setup/module/flexget/secrets.yml ~/flexget/secrets.yml")
    os.system("cp /home/osmc/Documents/rpi_setup/module/flexget/secrets.yml ~/flexget/config.yml")
    os.system("cp -r /home/osmc/Documents/rpi_setup/module/flexget/plugins ~/flexget/plugins")
    os.system("cd /home/osmc/Documents/rpi_setup/module/flexget")
    os.system('sed -i "s/yourtraktusername/'+c.trakt_user+'/g" /home/osmc/flexget/autosetup.sh')
    os.system("bash ~/flexget/autosetup.sh")
    os.system("sudo systemctl stop transmission")
    os.system("cd ~/.config/transmission")
    with open("~/.config/transmission/runflexget.sh", 'w+') as new_file:
        new_file.write("~/flexget/bin/flexget execute --tasks find-* move-*")
    os.system("chmod +x runflexget.sh")
    os.system("sudo systemctl start transmission")
    # final_output += sick_rage.install(c.sickrage_name, c.sickrage_pass, c.download_dir, c.series_dir, c.trakt_user, c.transmission_user, c.transmission_pass)

if c.install_sickrage == 'yes':
    print("INSTALLING SickRage!")
    if not transmission_installed:
        final_output += transmission.install(c.disk_name, c.transmission_user, c.transmission_pass, c.download_dir)
        transmission_installed = True
    final_output += sick_rage.install(c.sickrage_name, c.sickrage_pass, c.download_dir, c.series_dir, c.trakt_user, c.transmission_user, c.transmission_pass)

if c.install_potato == 'yes':
    print("INSTALLING CouchPotato!")
    if not transmission_installed:
        final_output += transmission.install(c.disk_name, c.transmission_user, c.transmission_pass, c.download_dir)
        transmission_installed = True
    final_output += couchpotato.install()

if c.install_nextcloudpi == 'yes':
    print("INSTALLING Next Cloud!")
    final_output += next_cloud.install()

# if hf.do_you_want('Install RADARR? (Software to download movies)'):
#     print("INSTALLING RADARR!")
#     if not transmission_installed:
#         final_output += transmission.install(c.disk_name, user_name, c.download_dir)
#         transmission_installed = True
#     final_output += radarr.install(user_name)

# if hf.do_you_want('Install ZSH? (Cool terminal)'):
#     print("INSTALLING ZSH!")
#     zsh.install()

if c.change_pass == 'yes':
    os.system("passwd")

with open(".credentials.txt", 'w') as new_file:
    new_file.write(final_output)

if hf.do_you_want('Reboot (recomended)?'):
    os.system("sudo reboot")

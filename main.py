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

#INSTALL MANDATORY STUFF
os.system("sudo apt-get update")
if os.system("git --version") != 0:
    print("INSTALLING git.")
    os.system("sudo apt-get install git -y")

if c.install_spotify == 'yes':
    print("INSTALLING SPOTIFY!")
    final_output += spotify.install(c.spotify_name)

if c.install_sickrage == 'yes':
    print("INSTALLING SickRage!")
    if not transmission_installed:
        final_output += transmission.install(c.disk_name, c.transmission_user, c.transmission_pass)
        transmission_installed = True
    final_output += sick_rage.install(c.sickrage_name, c.sickrage_pass, c.download_dir, c.series_dir, c.trakt_user, c.transmission_user, c.transmission_pass)

if hf.do_you_want('Install CouchPotato? (Software to download movies)'):
    print("INSTALLING CouchPotato!")
    if not transmission_installed:
        final_output += transmission.install(c.disk_name, c.transmission_user, c.transmission_pass)
        transmission_installed = True
    final_output += couchpotato.install()

if hf.do_you_want('Install next nextcloudpi? (kinda google drive)'):
    print("INSTALLING Next Cloud!")
    final_output += next_cloud.install()

# if hf.do_you_want('Install RADARR? (Software to download movies)'):
#     print("INSTALLING RADARR!")
#     if not transmission_installed:
#         final_output += transmission.install(c.disk_name, user_name)
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

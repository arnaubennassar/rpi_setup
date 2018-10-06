import os
import getpass
import helper_functions as hf
import module.spotify as spotify
import module.transmission as transmission
import module.sick_rage as sick_rage
import module.radarr as radarr
import module.zsh as zsh

transmission_installed = False
user_name = getpass.getuser()
final_output = ''

#INSTALL MANDATORY STUFF
os.system("sudo apt-get update")
if os.system("git --version") != 0:
    print("INSTALLING git.")
    os.system("sudo apt-get install git -y")

disk_name = hf.input_w_confirmation('Introduce the mame of the disk you want to use. (If you dont want to download stuff put something random.): ', 'The disk name will be: ')

if hf.do_you_want('Change password?'):
    os.system("passwd")

if hf.do_you_want('Install SPOTIFY connect? (client to use as remote speaker)'):
    print("INSTALLING SPOTIFY!")
    final_output += spotify.install()

if hf.do_you_want('Install SickRage? (Software to download series)'):
    print("INSTALLING SickRage!")
    if not transmission_installed:
        final_output += transmission.install(disk_name, user_name)
        transmission_installed = True
    final_output += sick_rage.install(user_name)

if hf.do_you_want('Install RADARR? (Software to download movies)'):
    print("INSTALLING RADARR!")
    if not transmission_installed:
        final_output += transmission.install(disk_name, user_name)
        transmission_installed = True
    final_output += radarr.install(user_name)

if hf.do_you_want('Install ZSH? (Cool terminal)'):
    print("INSTALLING ZSH!")
    zsh.install()

with open(".credentials.txt", 'w+') as new_file:
    new_file.write(final_output)

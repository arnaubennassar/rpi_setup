import helper_functions as hf
import os

def install(user_name):
    # if os.system("") == 0:
    #     print("SICK RAGE ALREADY INSTALLED.")
    #     return ''
    sick_user = hf.input_w_confirmation('Input SiCKRAGE user name: ', 'The SiCKRAGE user will be: ')
    sick_pass = hf.input_w_confirmation('Input SiCKRAGE user password: ', 'The SiCKRAGE password will be: ')
    os.system("sudo apt-get --yes --force-yes install p7zip-full")
    os.system("wget http://sourceforge.net/projects/bananapi/files/unrar_5.2.6-1_armhf.deb")
    os.system("sudo dpkg -i unrar_5.2.6-1_armhf.deb")
    os.system("rm  unrar_5.2.6-1_armhf.deb")
    os.system("sudo useradd sickrage")
    os.system("sudo usermod -a -G osmc sickrage")
    os.system("sudo git clone https://github.com/SiCKRAGE/SickRage.git /opt/sickrage")
    os.system("sudo cp /opt/sickrage/runscripts/init.systemd /etc/systemd/system/sickrage.service")
    os.system("sudo chown -R sickrage:sickrage /opt/sickrage")
    os.system("sudo chmod +x /opt/sickrage")
    os.system("sudo chmod a-x /etc/systemd/system/sickrage.service")
    os.system("cd /etc/systemd/system")
    os.system("sudo sed -i 's@/usr/bin/python2.7 /opt/sickrage/SickBeard.py -q --daemon --nolaunch --datadir=/opt/sickrage@/opt/sickrage/SickBeard.py -q --daemon --nolaunch --datadir=/opt/sickrage@g' sickrage.service")
    os.system("sudo systemctl enable sickrage.service")
    os.system("sudo systemctl start sickrage.service")
    os.system("sudo service sickrage stop")
    os.system("cd /opt/sickrage/")
    os.system("""sudo sed -i 's@web_username = ""@web_username = """+'"'+sick_user+'"'+"""@g' config.ini""")
    os.system("""sudo sed -i 's@web_password = ""@web_password = """+'"'+sick_pass+'"'+"""@g' config.ini""")
    os.system("sudo service sickrage start")
    return """
    ----- SiCKRAGE:
        user: """+sick_user+"""
        pass: """+sick_pass+"""
        port: 8081
    """

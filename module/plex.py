import os

def install():
    os.system("sudo apt-get install apt-transport-https -y --force-yes")
    os.system("wget -O - https://dev2day.de/pms/dev2day-pms.gpg.key | sudo apt-key add -")
    os.system('echo "deb https://dev2day.de/pms/ stretch main" | sudo tee /etc/apt/sources.list.d/pms.list')
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -t stretch plexmediaserver-installer -y")
    

#!/bin/bash
#INIT
device_name_response=nope
while [ "$device_name_response" != "yes" ]
do
  echo "Whats the name your gonna give to this device?"
  read device_name
  echo "Your device name will be: $device_name. Are you happy with it? (yes/no)"
  read device_name_response
done
#INSTALL mandatory stuff
echo "___________________________"
echo "UPDATING"
apt-get update -y
if [ $? -eq 0 ]
then
    echo "___________________________"
    echo "DONE UPDATING"
else
    echo "PLEAS RUN AS ROOT (sudo)"
    exit 1
fi
apt-get install git -y
if [ $? -eq 0 ]
then
    echo "___________________________"
    echo "DONE INSTALLING GIT"
else
    echo "___________________________"
    echo "GIT not installed"
fi
#install plugins
echo "___________________________"
echo "LET'S GO FOR THE PLUGINS"

echo "LET'S GO FOR SPOTIFY!"
spotyfy_response=nope
while [ "$spotyfy_response" != "yes" ] && [ $spotyfy_response != "no" ]
do
  echo "should I install spotify, client for spotify connect? (yes/no)"
  read spotyfy_response
done
if [ "$spotyfy_response" = "yes" ];
then
  echo "___________________________"
  echo "INSTALLING SPOTIFY"
  apt-get -y install apt-transport-https
  curl -sSL https://dtcooper.github.io/raspotify/key.asc | apt-key add -v -
  echo 'deb https://dtcooper.github.io/raspotify jessie main' | tee /etc/apt/sources.list.d/raspotify.list
  apt-get update
  apt-get install apt-transport-https
  apt-get -y install raspotify
  if [ $? -eq 0 ]
  then
      #Set max quality and device name
      echo "DEVICE_NAME=\"$device_name\" \nBITRATE=\"320\"" >> /etc/default/raspotify
      systemctl restart raspotify
      echo "DONE INSTALLING SPOTIFY!!"
  else
      echo "___________________________"
      echo "SPOTIFY NOT INSTALLED :("
  fi
fi


echo "LET'S GO FOR SICKRAGE!"
sickrage_response=nope
while [ "$sickrage_response" != "yes" ] && [ $sickrage_response != "no" ]
do
  echo "should I install sickrage, client for automated tv show downloads? (yes/no)"
  read sickrage_response
done
if [ "$sickrage_response" = "yes" ];
then
  echo "___________________________"
  echo "INSTALING SICKRAGE!"
  echo "begining installing p7zip..."
  apt-get --yes --force-yes install p7zip-full
  echo "installed p7zip"
  echo "begining installing unrar..."
  wget http://sourceforge.net/projects/bananapi/files/unrar_5.2.6-1_armhf.deb
  dpkg -i unrar_5.2.6-1_armhf.deb
  echo "successfully installed and removing temporary file of unrar"
  rm  unrar_5.2.6-1_armhf.deb
  echo "removed temporary file of unrar"
  echo "Begining to install SickRage"
  echo "creating sickrage username and adding to group..."
  useradd sickrage
  usermod -a -G osmc sickrage
  echo "downloading sickrage and installing..."
  git clone https://github.com/SiCKRAGE/SickRage.git /opt/sickrage
  echo "creating startup script for sickrage..."
  cp /opt/sickrage/runscripts/init.systemd /etc/systemd/system/sickrage.service
  echo "granting permissions to sickrage folder"
  chown -R sickrage:sickrage /opt/sickrage
  chmod +x /opt/sickrage
  chmod a-x /etc/systemd/system/sickrage.service
  echo "fixing path at startup script..."
  cd /etc/systemd/system
  sed -i 's@/usr/bin/python2.7 /opt/sickrage/SickBeard.py -q --daemon --nolaunch --datadir=/opt/sickrage@/opt/sickrage/SickBeard.py -q --daemon --nolaunch --datadir=/opt/sickrage@g' sickrage.service
  echo "enabling startup script...."
  systemctl enable sickrage.service
  echo "starting sickrage and waiting to create file config.ini ..."
  systemctl start sickrage.service
  echo "created file config.ini and stopping sickrage..."
  service sickrage stop
  cd /opt/sickrage/
  echo "adding username and password to sickrage... this fixes freezing raspbeery pi when you try to login to sickrage..."
  sed -i 's@web_username = ""@web_username = "osmc"@g' config.ini
  sed -i 's@web_password = ""@web_password = "osmc"@g' config.ini
  echo "Sickrage succesfully installed..."
  service sickrage start
  echo "Sickrage service started!"
  echo " "
  echo "Successfully installed! more info bellow..."
  echo " "
  echo "couchpotato info:"
  echo "webgui raspberry_ip:5050"
  echo " "
  echo "sickrage info:"
  echo "webgui raspberry_ip:8081"
  echo " "
  echo "sickrage login info:"
  echo " "
  echo "username: osmc"
  echo "password: osmc"
  echo " "
  echo "enjoy"
fi


echo "LET'S GO FOR SICKRAGE!"
radarr_response=nope
while [ "$radarr_response" != "yes" ] && [ $radarr_response != "no" ]
do
  echo "should I install radarr, client for automated movie downloads? (yes/no)"
  read radarr_response
done
if [ "$radarr_response" = "yes" ];
then
  echo "___________________________"
  echo "INSTALING RADARR!"
  apt install mono-devel mediainfo sqlite3 libmono-cil-dev -y
  # apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
  # echo "deb http://download.mono-project.com/repo/debian jessie main" | tee /etc/apt/sources.list.d/mono-xamarin.list
  cd /tmp
  wget https://github.com/Radarr/Radarr/releases/download/v0.2.0.1120/Radarr.develop.0.2.0.1120.linux.tar.gz
  tar -xvf Radarr* -C /opt/
  chown -R osmc:osmc /opt/Radarr
  echo "[Unit]\nDescription=Radarr Daemon\nAfter=syslog.target network.target\n\n[Service]\nUser=osmc\nGroup=osmc\n\nType=simple\nExecStart=/usr/bin/mono /opt/Radarr/Radarr.exe --nobrowser\nTimeoutStopSec=20\nKillMode=process\nRestart=on-failure\n\n[Install]\nWantedBy=multi-user.target" >> /etc/systemd/system/radarr.service
  systemctl enable radarr
  systemctl start radarr
  echo "radarr installed acces it through the port :7878"
fi



echo "___________________________"
echo "INSTALLING ZSH"
apt-get install zsh
chsh -s $(which zsh)
usermod -s /bin/bash $SUDO_USER
if [ $? -eq 0 ]
then
    echo "___________________________"
    echo "DONE INSTALLING ZSH"
else
    echo "___________________________"
    echo "ZSH not installed"
    echo "___________________________"
fi
echo "INSTALLING OH-MY-ZSH"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
if [ $? -eq 0 ]
then
    echo "___________________________"
    echo "DONE INSTALLING OH-MY-ZSH"
else
    echo "___________________________"
    echo "OH-MY-ZSH not installed"
fi
return 0

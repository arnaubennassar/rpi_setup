#!/bin/bash
#INIT

transmission()
{
  echo "FIRST LETS INSTALL TRANSMISSION"
  transmission_user_response=nope
  while [ "$transmission_user_response" != "yes" ]
  do
    echo "Username for transmisssion (torrent client)?"
    read transmission_user
    echo "Your transmission name will be: $transmission_user. Are you happy with it? (yes/no)"
    read transmission_user_response
  done
  transmission_pass_response=nope
  while [ "$transmission_pass_response" != "yes" ]
  do
    echo "Password for transmisssion (torrent client)?"
    read transmission_pass
    echo "Your transmission password will be: $transmission_pass. Are you happy with it? (yes/no)"
    read transmission_pass_response
  done
  apt-get install transmission-daemon -y
  mkdir /media/$disk_name/DOWNLOADS
  mkdir /media/$disk_name/incomplete_downloads
  echo "{\n
    \"alt-speed-down\": 50,\n
    \"alt-speed-enabled\": false,\n
    \"alt-speed-time-begin\": 540,\n
    \"alt-speed-time-day\": 127,\n
    \"alt-speed-time-enabled\": false,\n
    \"alt-speed-time-end\": 1020,\n
    \"alt-speed-up\": 50,\n
    \"bind-address-ipv4\": \"0.0.0.0\",\n
    \"bind-address-ipv6\": \"::\",\n
    \"blocklist-enabled\": false,\n
    \"blocklist-url\": \"http://www.example.com/blocklist\",\n
    \"cache-size-mb\": 10,\n
    \"dht-enabled\": true,\n
    \"download-dir\": \"/media/$disk_name/DOWNLOADS\",\n
    \"download-limit\": 100,\n
    \"download-limit-enabled\": 0,\n
    \"download-queue-enabled\": true,\n
    \"download-queue-size\": 5,\n
    \"encryption\": 1,\n
    \"idle-seeding-limit\": 30,\n
    \"idle-seeding-limit-enabled\": false,\n
    \"incomplete-dir\": \"/media/$disk_name/incomplete_downloads\",\n
    \"incomplete-dir-enabled\": true,\n
    \"lpd-enabled\": false,\n
    \"max-peers-global\": 200,\n
    \"message-level\": 1,\n
    \"peer-congestion-algorithm\": \"\",\n
    \"peer-id-ttl-hours\": 6,\n
    \"peer-limit-global\": 200,\n
    \"peer-limit-per-torrent\": 50,\n
    \"peer-port\": 51413,\n
    \"peer-port-random-high\": 65535,\n
    \"peer-port-random-low\": 49152,\n
    \"peer-port-random-on-start\": false,\n
    \"peer-socket-tos\": \"default\",\n
    \"pex-enabled\": true,\n
    \"port-forwarding-enabled\": false,\n
    \"preallocation\": 2,\n
    \"prefetch-enabled\": true,\n
    \"queue-stalled-enabled\": true,\n
    \"queue-stalled-minutes\": 30,\n
    \"ratio-limit\": 2,\n
    \"ratio-limit-enabled\": false,\n
    \"rename-partial-files\": true,\n
    \"rpc-authentication-required\": true,\n
    \"rpc-bind-address\": \"0.0.0.0\",\n
    \"rpc-enabled\": true,\n
    \"rpc-host-whitelist\": \"\",\n
    \"rpc-host-whitelist-enabled\": true,\n
    \"rpc-password\": \"$transmission_pass\",\n
    \"rpc-port\": 9091,\n
    \"rpc-url\": \"/transmission/\",\n
    \"rpc-username\": \"$transmission_user\",\n
    \"rpc-whitelist\": \"*.*.*.*\",\n
    \"rpc-whitelist-enabled\": true,\n
    \"scrape-paused-torrents-enabled\": true,\n
    \"script-torrent-done-enabled\": false,\n
    \"script-torrent-done-filename\": \"\",\n
    \"seed-queue-enabled\": false,\n
    \"seed-queue-size\": 10,\n
    \"speed-limit-down\": 100,\n
    \"speed-limit-down-enabled\": false,\n
    \"speed-limit-up\": 100,\n
    \"speed-limit-up-enabled\": false,\n
    \"start-added-torrents\": true,\n
    \"trash-original-torrent-files\": false,\n
    \"umask\": 2,\n
    \"upload-limit\": 100,\n
    \"upload-limit-enabled\": 0,\n
    \"upload-slots-per-torrent\": 14,\n
    \"utp-enabled\": true\n}" >> /etc/transmission-daemon/settings.json
  chmod g+rw /media/$disk_name/incomplete_downloads
  chgrp -R $SUDO_USER /media/$disk_name/DOWNLOADS
  usermod -a -G $SUDO_USER debian-transmission
  /etc/init.d/transmission-daemon start
  final_output="$final_output\nTRANSMISSION:\n    user:$transmission_user\n    pass:$transmission_pass\n    port:8081"
}
final_output=""
device_name_response=nope
transmission_installed="false"
while [ "$device_name_response" != "yes" ]
do
  echo "Whats the name your gonna give to this device?"
  read device_name
  echo "Your device name will be: $device_name. Are you happy with it? (yes/no)"
  read device_name_response
done
disk_name_response=nope
while [ "$disk_name_response" != "yes" ]
do
  echo "Whats the name of the disk? (put something random if you dont pretend to use any)"
  read disk_name
  echo "Your disk name will be: $disk_name. Are you happy with it? (yes/no)"
  read disk_name_response
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
  if [ "$transmission_installed" = "false" ];
  then
    transmission
    transmission_installed="true"
  fi
  sickrage_user_response=nope
  while [ "$sickrage_user_response" != "yes" ]
  do
    echo "Username for SiCKRAGE ?"
    read sickrage_name
    echo "Your SiCKRAGE name will be: $sickrage_name. Are you happy with it? (yes/no)"
    read sickrage_user_response
  done
  sickrage_pass_response=nope
  while [ "$sickrage_pass_response" != "yes" ]
  do
    echo "Password for sickrage?"
    read sickrage_pass
    echo "Your sickrage password will be: $sickrage_pass. Are you happy with it? (yes/no)"
    read sickrage_pass_response
  done
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
  echo "username: $sickrage_user"
  echo "password: $sickrage_pass"
  echo " "
  echo "enjoy"
  final_output="$final_output\nSICKRAGE:\n    user:$sickrage_user\n    pass:$sickrage_pass\n    port:8081"
fi


echo "LET'S GO FOR RADARR!"
radarr_response=nope
while [ "$radarr_response" != "yes" ] && [ $radarr_response != "no" ]
do
  echo "should I install radarr, client for automated movie downloads? (yes/no)"
  read radarr_response
done
if [ "$radarr_response" = "yes" ];
then
  if [ "$transmission_installed" = "false" ];
  then
    transmission
    transmission_installed="true"
  fi
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
  final_output="$final_output\nRADARR:\n    port:7878"
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
runuser -l $SUDO_USER -c 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/coreycole/oh-my-zsh/master/tools/install.sh)"'
chsh -s $(which zsh) $SUDO_USER
if [ $? -eq 0 ]
then
    echo "___________________________"
    echo "DONE INSTALLING OH-MY-ZSH"
else
    echo "___________________________"
    echo "OH-MY-ZSH not installed"
fi
echo final_output
return 0

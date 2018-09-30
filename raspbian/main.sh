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
echo "___________________________"
echo "INSTALLING ZSH"
apt-get install zsh
chsh -s $(which zsh)
if [ $? -eq 0 ]
then
    echo "___________________________"
    echo "DONE INSTALLING ZSH"
else
    echo "___________________________"
    echo "ZSH not installed"
    echo "___________________________"
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
  curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
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
echo "DONE!! LET'S REBOOT"
reboot

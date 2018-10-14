import os

def install(shows_dir, movies_dir, trakt_user, transmission_user, transmission_pass, download_dir):
    media_config = """<sources>
    <programs>
        <default pathversion="1"></default>
    </programs>
    <video>
        <default pathversion="1"></default>
        <source>
            <name>TV Shows</name>
            <path pathversion="1">"""+shows_dir+"""</path>
            <allowsharing>true</allowsharing>
        </source>
        <source>
            <name>Movies</name>
            <path pathversion="1">"""+movies_dir+"""</path>
            <allowsharing>true</allowsharing>
        </source>
    </video>
    <music>
        <default pathversion="1"></default>
        <source>
            <name>Music</name>
            <path pathversion="1">/media/</path>
            <allowsharing>true</allowsharing>
        </source>
    </music>
    <pictures>
        <default pathversion="1"></default>
        <source>
            <name>Pictures</name>
            <path pathversion="1">/media/</path>
            <allowsharing>true</allowsharing>
        </source>
    </pictures>
    <files>
        <default pathversion="1"></default>
    </files>
</sources>"""
    with open("/home/osmc/.kodi/userdata/sources.xml", 'w+') as new_file:
        new_file.write(media_config)

    os.system("sudo apt-get -y install python3")
    os.system("")
    os.system("")
    os.system("")
    os.system("")
    os.system("")
    os.system("")

sudo apt-get -y install python3-pip
sudo apt-get install -y python3-libtorrent
sudo pip3 install --upgrade setuptools
sudo pip3 install virtualenv
virtualenv --system-site-packages -p python3 $HomeFolder/flexget/
cd $HomeFolder/flexget/
bin/pip install flexget
source ~/flexget/bin/activate
pip3 install subliminal>=2.0
pip3 install transmissionrpc
pip3 install transmissionrpc --upgrade
wget -O config.yml https://rawgit.com/zilexa/flexget_config/master/config.yml
wget -O secrets.yml https://rawgit.com/zilexa/flexget_config/master/secrets.yml
sed -i "s/TraktUser/$TraktUser/g" $HomeFolder/flexget/secrets.yml
sed -i "s/TransmissionUser/$TransmissionUser/g" $HomeFolder/flexget/secrets.yml
sed -i "s/TransmissionPw/$TransmissionPw/g" $HomeFolder/flexget/secrets.yml
sed -i 's|media/RootOfMedia/|'$MediaFolder/'|g' $HomeFolder/flexget/secrets.yml
sudo mkdir $HomeFolder/flexget/plugins/
cd $HomeFolder/flexget/plugins/
sudo wget -O log_filter.py https://rawgit.com/zilexa/flexget_config/master/plugins/log_filter.py


    os.system("cd /home/osmc/Documents/rpi_setup/module/flexget")
    os.system("sudo pip install --upgrade setuptools")
    os.system("sudo apt-get install -y python3-libtorrent")
    os.system("pip install flexget")
    os.system("pip install subliminal>=2.0")
    os.system("pip install transmissionrpc")
    os.system("pip install transmissionrpc --upgrade")
    config_file = """[Unit]
Description=Flexget Daemon
After=network.target
[Service]
Type=simple
User=osmc
UMask=000
WorkingDirectory=/home/osmc/Documents/rpi_setup/flexget
ExecStart=/home/osmc/Documents/rpi_setup/flexget/bin/flexget daemon start --autoreload-config
ExecStop=/home/osmc/Documents/rpi_setup/flexget/bin/flexget daemon stop
ExecReload=/home/osmc/Documents/rpi_setup/flexget/bin/flexget daemon reload
[Install]
WantedBy=multi-user.target"""
    with open("tmp_settings.service", 'w+') as new_file:
        new_file.write(config_file)
    os.system("sudo mv tmp_settings.service /lib/systemd/system/flexget.service")
    os.system("sudo chmod 755 /lib/systemd/system/flexget.service")
    os.system("sudo systemctl enable flexget")
    os.system("~/Documents/rpi_setup/flexget/bin/flexget trakt auth "+trakt_user)

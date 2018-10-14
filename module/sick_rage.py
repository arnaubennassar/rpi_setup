import helper_functions as hf
import os

def install():
    os.system("cd ~")
    os.system("sudo git clone https://github.com/SickRage/SickRage.git /opt/sickrage")
    os.system("sudo chown osmc:osmc /opt/sickrage -R")
    config_file = """[Unit]
Description=SickRage Daemon
After=network.target auditd.service

[Service]
User=osmc
Group=osmc
Type=forking
PIDFile=/run/sickrage.pid
ExecStart=/usr/bin/python2.7 /opt/sickrage/SiCKRAGE.py -q --daemon --pidfile /run/sickrage.pid --nolaunch --datadir=/opt/sickrage
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target"""
    with open("tmp_sick.service", 'w+') as new_file:
        new_file.write(config_file)
    os.system("sudo mv tmp_sick.service /etc/systemd/system/sickrage.service")
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl start sickrage")
    os.system("sudo systemctl enable sickrage")
    os.system("""echo -e "SickRage\nsickrage.service" | sudo tee /etc/osmc/apps.d/sickrage-app-osmc > /dev/null""")

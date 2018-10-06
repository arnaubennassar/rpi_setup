import os

def install():
    # os.system("sudo useradd couchpotato")
    # os.system("sudo usermod -a -G osmc couchpotato")
    # os.system("sudo mkdir /home/couchpotato")
    # os.system("sudo chown -R couchpotato:couchpotato /home/couchpotato")
    # os.system("sudo git clone http://github.com/RuudBurger/CouchPotatoServer /opt/CouchPotatoServer")
    # os.system("sudo chown -R couchpotato:couchpotato /opt/CouchPotatoServer")
    os.system("sudo cp /opt/CouchPotatoServer/init/couchpotato.fedora.service /opt/CouchPotatoServer/init/couchpotato.service")
    cp_config = """
    [Unit]
    Description=CouchPotato application instance
    After=network-online.target

    [Service]
    ExecStart=/opt/CouchPotatoServer/CouchPotato.py --daemon
    GuessMainPID=no
    Type=forking
    User=couchpotato
    Group=couchpotato
    KillMode=process

    [Install]
WantedBy=multi-user.target"""
    with open("tmp_cp", 'w+') as new_file:
        new_file.write(cp_config)
    os.system("sudo mv tmp_cp /opt/CouchPotatoServer/init/couchpotato.service")
    os.system("sudo cp /opt/CouchPotatoServer/init/couchpotato.service /etc/systemd/system/couchpotato.service")
    os.system("sudo systemctl enable couchpotato.service")
    os.system("sudo systemctl start couchpotato.service")
    return """
    ----- CouchPotato:
        port: 5050
    """

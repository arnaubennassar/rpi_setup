import os

def install(user_name):
    if os.system("sudo systemctl status radarr") == 0:
        print("RADARR ALREADY INSTALLED.")
        return ''
    os.system("sudo apt install mono-devel mediainfo sqlite3 libmono-cil-dev -y")
    os.system("cd /tmp")
    os.system("wget https://github.com/Radarr/Radarr/releases/download/v0.2.0.1120/Radarr.develop.0.2.0.1120.linux.tar.gz")
    os.system("tar -xvf Radarr* -C /opt/")
    os.system("sudo chown -R osmc:osmc /opt/Radarr")
    radarr_config = """[Unit]
    Description=Radarr Daemon
    After=syslog.target network.target

    [Service]
    User="""+user_name+"""
    Group=osmc
    Type=simpe
    ExecStart=/usr/bin/mono /opt/Radarr/Radarr.exe --nobrowser
    TimeoutStopSec=20
    KillMode=process
    Restart=on-failure

    [Install]
    WantedBy=multi-user.target"""
    with open("/etc/systemd/system/radarr.service", 'w+') as new_file:
        new_file.write(radarr_config)
    os.system("sudo systemctl enable radarr")
    os.system("sudo systemctl start radarr")
    return """
    ----- RADARR:
        port: 7878
    """

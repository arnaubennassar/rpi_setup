import os
import helper_functions as hf

def install(disk_name, transmission_user, transmission_pass, download_dir):
    if os.system("transmission-daemon -V") == 0:
        print("TRANSMISSION ALREADY INSTALLED.")
        return ''
    print("FIRST LETS INSTALL TRANSMISSION")
    os.system("sudo apt-get install transmission-daemon -y")
    os.system("sudo chmod g+rw /media/"+disk_name+"/incomplete_downloads")
    os.system("sudo chgrp -R osmc /media/"+disk_name+"/DOWNLOADS")
    os.system("sudo usermod -a -G osmc debian-transmission")
    os.system("sudo /etc/init.d/transmission-daemon start")
    os.system("sudo /etc/init.d/transmission-daemon stop")
    config_file = """{
        \"alt-speed-down\": 50,
        \"alt-speed-enabled\": false,
        \"alt-speed-time-begin\": 540,
        \"alt-speed-time-day\": 127,
        \"alt-speed-time-enabled\": false,
        \"alt-speed-time-end\": 1020,
        \"alt-speed-up\": 50,
        \"bind-address-ipv4\": \"0.0.0.0\",
        \"bind-address-ipv6\": \"::\",
        \"blocklist-enabled\": false,
        \"blocklist-url\": \"http://www.example.com/blocklist\",
        \"cache-size-mb\": 10,
        \"dht-enabled\": true,
        \"download-dir\": \""""+download_dir+"""\",
        \"download-limit\": 100,
        \"download-limit-enabled\": 0,
        \"download-queue-enabled\": true,
        \"download-queue-size\": 5,
        \"encryption\": 1,
        \"idle-seeding-limit\": 30,
        \"idle-seeding-limit-enabled\": false,
        \"incomplete-dir\": \"/media/"""+disk_name+"""/incomplete_downloads\",
        \"incomplete-dir-enabled\": true,
        \"lpd-enabled\": false,
        \"max-peers-global\": 200,
        \"message-level\": 1,
        \"peer-congestion-algorithm\": \"\",
        \"peer-id-ttl-hours\": 6,
        \"peer-limit-global\": 200,
        \"peer-limit-per-torrent\": 50,
        \"peer-port\": 51413,
        \"peer-port-random-high\": 65535,
        \"peer-port-random-low\": 49152,
        \"peer-port-random-on-start\": false,
        \"peer-socket-tos\": \"default\",
        \"pex-enabled\": true,
        \"port-forwarding-enabled\": false,
        \"preallocation\": 2,
        \"prefetch-enabled\": true,
        \"queue-stalled-enabled\": true,
        \"queue-stalled-minutes\": 30,
        \"ratio-limit\": 2,
        \"ratio-limit-enabled\": false,
        \"rename-partial-files\": true,
        \"rpc-authentication-required\": true,
        \"rpc-bind-address\": \"0.0.0.0\",
        \"rpc-enabled\": true,
        \"rpc-host-whitelist\": \"\",
        \"rpc-host-whitelist-enabled\": true,
        \"rpc-password\": \""""+transmission_pass+"""\",
        \"rpc-port\": 9091,
        \"rpc-url\": \"/transmission/\",
        \"rpc-username\": \""""+transmission_user+"""\",
        \"rpc-whitelist\": \"*.*.*.*\",
        \"rpc-whitelist-enabled\": true,
        \"scrape-paused-torrents-enabled\": true,
        \"script-torrent-done-enabled\": true,
        \"script-torrent-done-filename\": \"~/.config/transmission-daemon/runflexget.sh\",
        \"seed-queue-enabled\": false,
        \"seed-queue-size\": 10,
        \"speed-limit-down\": 100,
        \"speed-limit-down-enabled\": false,
        \"speed-limit-up\": 100,
        \"speed-limit-up-enabled\": false,
        \"start-added-torrents\": true,
        \"trash-original-torrent-files\": false,
        \"umask\": 2,
        \"upload-limit\": 100,
        \"upload-limit-enabled\": 0,
        \"upload-slots-per-torrent\": 14,
        \"utp-enabled\": true
    }"""
    with open("tmp_settings.json", 'w+') as new_file:
        new_file.write(config_file)
    os.system("sudo mv tmp_settings.json /etc/transmission-daemon/settings.json")
    os.system("sudo /etc/init.d/transmission-daemon start")


    return """
    ----- TRANSMISSION:
        user: """+transmission_user+"""
        pass: """+transmission_pass+"""
        port: 9091
    """

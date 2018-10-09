import os
import helper_functions as hf

def install(spotify_name):
    # if os.system("sudo systemctl status raspotify") == 0:
    #     print("SPOTIFY ALREADY INSTALLED.")
    #     return ''
    os.system("sudo apt-get -y install apt-transport-https")
    os.system("curl -sSL https://dtcooper.github.io/raspotify/key.asc | sudo apt-key add -v -")
    os.system("echo 'deb https://dtcooper.github.io/raspotify jessie main' | sudo tee /etc/apt/sources.list.d/raspotify.list")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install apt-transport-https")
    os.system("sudo apt-get -y install raspotify")
    spotify_config = """DEVICE_NAME="""+spotify_name+"""
    BITRATE="320"
    #"""
    with open("tmp_raspotify", 'w+') as new_file:
        new_file.write(spotify_config)
    os.system("sudo mv tmp_raspotify /etc/default/raspotify")
    os.system("sudo systemctl restart raspotify")
    return """
    ----- SPOTIFY:
        device name: """+spotify_name+"""
    """

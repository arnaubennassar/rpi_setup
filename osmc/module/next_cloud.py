import os

def install():
    os.system("sudo curl -sSL https://raw.githubusercontent.com/nextcloud/nextcloudpi/master/install.sh | bash")
    return """
    ----- NextCloudPi:
    """

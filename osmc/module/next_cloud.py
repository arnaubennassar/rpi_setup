import os

def install():
    os.system("sudo apt update -y")
    os.system("sudo apt install ca-certificates apt-transport-https -y")
    os.system("wget -q https://packages.sury.org/php/apt.gpg -O- | sudo apt-key add -")
    os.system("""echo "deb https://packages.sury.org/php/ stretch main" | sudo tee /etc/apt/sources.list.d/php.list""")
    os.system("sudo apt update -y")
    os.system("sudo apt install php7.2 -y")
    os.system("sudo apt install php7.2-cli php7.2-common php7.2-curl php7.2-mbstring php7.2-mysql php7.2-xml  php7.2-bz2 php7.2-fpm php7.2-gd php7.2-intl php7.2-ldap php7.2-zip -y")
    os.system("""echo "Raspbian GNU/Linux 9" | sudo tee  /etc/issue""")
    os.system("curl -sSL https://raw.githubusercontent.com/nextcloud/nextcloudpi/master/install.sh | sudo bash")
    os.system("nc-init")
    return """
    ----- NextCloudPi:
    """

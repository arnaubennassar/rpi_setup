import os

def install():
    os.system("sudo apt-get install zsh -y")
    os.system("chsh -s $(which zsh)")
    os.system("""sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\"""")

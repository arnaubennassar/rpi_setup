import os

def install():
    os.system("sudo apt-get install zsh -y")
    os.system("chsh -s $(which zsh)")
    install_command = """sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sed 's:env zsh::g' | sed 's:chsh -s .*$::g')"
    """
    os.system(install_command)

#Instructions for OSMC set up:

0. change remote port to 9999

0. Prepare DISK: format disk: sudo fdisk -l     sudo umount /dev/sda1       sudo mkfs.ext4 /dev/sda1 -L disk

1. Update the software:
> sudo apt-get update

2. Install git:
> sudo apt-get install git -y

3. Create a folder:
> mkdir Documents

4. Go for it:
> cd Documents

5. Clone this repo:
> git clone https://github.com/arnaubennassar/rpi_setup.git

6. move to the folder:
> cd rpi_setup

7. Duplicate the file config_template.py with the name config.py, and edit the new document with your set up preferences

8. execute the script:
> pyhton main.py

##After script
##Next cloud:
go to https://ip:443 (NOTE HTTPS!!)
user: ncp
skip auto assistant, and do it manualy (system info [thinder icon] have nice tips)
change pass for ncp and nc!!!

##couchpotato:
go to http://ip:5050

##sickrage:
go to https://ip:9091

2Vsb28wtp/BRNabeESsdX9EFZv/DTc7fuock5QdFscg
/Y7f2bXOEr4xEweBaGo6/6GlFmZImeshhdloyJZ2C9w

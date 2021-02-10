#!/bin/bash

g="\033[1;32m"
y="\033[1;33m"
w="\033[0;37m"
if [ -e chrome-remote-desktop_current_amd64.deb ]
then
    sudo dpkg --install chrome-remote-desktop_current_amd64.deb
    sudo apt install --assume-yes --fix-broken
else
    wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb 
    sudo dpkg --install chrome-remote-desktop_current_amd64.deb
    sudo apt install --assume-yes --fix-broken
fi
DEBIAN_FRONTEND=noninteractive
apt install --assume-yes xfce4 desktop-base
sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'
sudo apt install --assume-yes xscreensaver
sudo apt install --assume-yes --fix-broken
sudo systemctl disable lightdm.service
if [ -e google-chrome-stable_current_amd64.deb ]
then

    sudo dpkg --install google-chrome-stable_current_amd64.deb
    sudo apt install --assume-yes --fix-broken
else
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
    sudo dpkg --install google-chrome-stable_current_amd64.deb
    sudo apt install --assume-yes --fix-broken
fi
sudo apt install nautilus nano -y
sudo adduser $USER chrome-remote-desktop
clear
echo -e "${w}  Visit: https://remotedesktop.google.com/headless"
read -p "   Command: " cmnd;
su - $USER -c """${cmnd}"""
echo -e "\n${g}[+] ${w}Selesai silahkan buka Aplikasi/Website Chrome Remote Desktop"

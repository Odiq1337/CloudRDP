import os
import sys


def Log(log):
    """
    Untuk mempermudah set warna

    !r: red/merah
    !g: green/hijau
    !w: white/putih
    !y: yellow:kuning

    """

    if "!r" in log:
        log = log.replace("!r", "\033[1;31m")
    if "!g" in log:
        log = log.replace("!g", "\033[1;32m")
    if "!w" in log:
        log = log.replace("!w", "\033[0;37m")

    if "!y" in log:
        log = log.replace("!y", "\033[1;33m")

    if "!b" in log:
        log = log.replace("!b", "\033[0;34m")

    return(log)


def banner():
    os.system("clear")
    logo = """
       !y_____ _                 _   _____  _____  _____  
      / ____| |               | | |  __ \|  __ \|  __ \ 
     | |    | | ___  _   _  __| | | |__) | |  | | |__) |
     | |    | |/ _ \| | | |/ _` | |  _  /| |  | |  ___/ 
     | |____| | (_) | |_| | (_| | | | \ \| |__| | |     
      \_____|_|\___/ \__,_|\__,_| |_|  \_\_____/|_|     !w
                                                    
       https://github.com/Odiq1337/CloudRDP - By Odiq ©2020 v!b(1)!w
"""
    print(Log(logo))

class RDP(object):
    def __init__(self, p, u):
        self.username = u
        self.password = p
        print(Log("!b[+] !wMenginstall\n - Chrome Remote Desktop\n - Desktop Environment\n - Google Chrome\n - Other tools nano, nautilus"))
        self.installCRD()
        self.install_Desktop_environment()
        self.installGoogleChorme()
        self.installOtherTools()
        self.finish()


    def installCRD(self):
        os.system("wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb &> /dev/null")
        os.system("sudo dpkg --install chrome-remote-desktop_current_amd64.deb &> /dev/null")
        os.system("sudo apt install --assume-yes --fix-broken &> /dev/null")


    def install_Desktop_environment(self):
        os.system("DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base &> /dev/null")
        os.system("sudo bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session' &> /dev/null")
        os.system("sudo apt install --assume-yes xscreensaver &> /dev/null")
        os.system("sudo systemctl disable lightdm.service &> /dev/null")


    def installGoogleChorme(self):
        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &> /dev/null")
        os.system("sudo dpkg --install google-chrome-stable_current_amd64.deb &> /dev/null")
        os.system("sudo apt install --assume-yes --fix-broken &> /dev/null")


    def installOtherTools(self):
        os.system("apt install nautilus nano -y &> /dev/null")


    def finish(self):
        print(Log("!g[+] !wBerhasil menginstall"))
        os.system("sudo adduser %s chrome-remote-desktop &> /dev/null" % (self.username))
        print(Log("!wKunjungi https://remotedesktop.google.com/headless\nDan salin perintah Debian Linux"))
        code = input("Perintah: ")
        os.system('su - %s -c """%s"""' % (self.username, code))
        print(Log("!g[+] !wBerhasil silahkan check diaplikasi/website Chrome Remote Desktop"))
        while True:
            pass

if __name__ == "__main__":
    banner()
    password = input("Password root untuk RDP: ")
    RDP(password, sys.argv[1])

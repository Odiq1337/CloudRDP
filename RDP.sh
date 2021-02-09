user=$(whoami))

clear
echo -e "Bikin password root"
# untuk bikin password root baru
sudo passwd root


clear
echo -e "Masukkan password root yang tadi dibuat"
# login sebagai root
su


python RDP.py $user

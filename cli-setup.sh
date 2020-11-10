mkdir -p $HOME/.Dictionary_AV
cp data-orignal.json $HOME/.Dictionary_AV/data.json
cp random-picker.py $HOME/.Dictionary_AV/

echo "Want just a sudo password for installing dependencies ... "
sudo apt install figlet
sudo apt install python3
sudo apt install pip3
pip3 install json
pip3 install cdifflib

read -p "make a custom command [y/n] : " cmd

if [[ $cmd -ne "n" ]]
then
	sudo cp code.py /bin/dictionary
	echo "[+] command created !"
	echo "You can just hit enter to open up the distionary and /<command> for any of the commands to get execute !!"
fi

echo "Have a nice Day !"

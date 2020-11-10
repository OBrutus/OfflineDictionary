#!/bin/bash

cp ~/.bashrc ~/.Dictionary_AV/.bashrc.bak

echo "python3 ~/.Dictionary_AV/random-picker.py" >> ~/.bashrc

if [[ $? == 0 ]]
then
    echo "[+] Is Done"
fi
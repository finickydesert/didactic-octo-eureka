#!/usr/bin/env python3

# need python 3.10 at least to run
import os
from cryptography.fernet import Fernet

files = []
a = input("1: ubuntu update\n2:ubuntu upgrade\n3:tactical encrypt\n4:decrypt\n5:sudo\n6:arch\n7:Flatpak only\npress any other number to exit\n")
x = int(a)

def flatpak():
    os.system("sudo flatpak refresh; sudo flatpak update --assumeyes")


def encrypt():
    for file in os.listdir():
        if file == "thekey.key" or  file == "swiss_army_knife.py":
            continue
        if os.path.isfile(file):
                files.append(files)
        
    key = Fernet.generate_key()

    with open("thekey.key","wb") as thekey:
        thekey.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
       
def decrypt():
    for file in os.listdir():
        if file == "HACKING-SCRIPT.py" or file == "thekey.key" or file == "decrypt-script.py":
            continue
        if os.path.isfile(file):
            files.append(files)
        
    with open("thekey.key","rb") as key:
        secretkey = key.read()

    for file in files:
        with open(file, "rb") as thefile:
         contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    
def ubuntu_the_rest():
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")
    os.system("sudo apt autoremove -y")
    os.system("sudo snap refresh")
    flatpak()
    os.system("clear")
    os.system("neofetch")


def ubuntu_upgrade():
    os.system("sudo apt update")
    os.system("sudo apt dist-upgrade")
    os.system("sudo apt autoremove -y")
    os.system("sudo snap refresh")
    flatpak()

match x:
  case 1:
     ubuntu_the_rest()
  case 2:
    ubuntu_upgrade()
  case 3:
    encrypt()
  case 4:
    decrypt()
  case 5:
    os.system("clear")
    os.system("sudo -i")
  case 6:
    os.system("sudo pacman -Syuu")
    flatpak()
    os.system("neofetch")
  case 7:
    flatpak()
  

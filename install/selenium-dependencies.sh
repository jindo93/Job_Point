#!/usr/bin/env bash

# Assumes python3-pip is installed
# Assumes java8 is installed
### Update and Install
apt-get -y update
apt-get -y install unzip

### Remove existing downloads and binaries
sudo apt-get remove google-chrome-stable
rm ~/chromedriver_linux64.zip
rm /usr/local/bin/chromedriver

### Install Chrome
# Chrome version: 73.0.3683.86
# ChromeDriver version: 73.0.3683.68

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> 
/etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable

### Install ChromeDriver
wget -N http://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver

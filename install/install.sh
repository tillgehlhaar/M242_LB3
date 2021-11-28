#!/bin/bash
###################################################################
#File Name      : install.sh
#Description    : automated installation of Mosquitto.
#Args           :
#Author         : Sangeeth Sivakumaran
###################################################################
#default settings
sudo apt update -y && sudo apt install mosquitto mosquitto-clients -y
sudo systemctl status mosquitto
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
sudo systemctl restart mosquitto
sudo apt install python3 -y
sudo apt install python3-pip -y
pip install paho-mqtt
pip install mysql-connector
pip install mysql-connector-python
sudo mkdir logger
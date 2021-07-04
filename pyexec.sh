#!/bin/bash
cd server
sudo apt install python3.9-venv
python3.9 -m venv env
source env/bin/activate
sudo apt install python3-pip
sudo pip install Flask==1.1.2 
sudo pip install Flask-Cors==3.0.10
echo test
python3 app.py


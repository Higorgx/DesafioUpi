#!/bin/bash
cd server
source env/bin/activate
cd ..
cd client
sudo apt install npm
sudo npm install 
echo Testando
sudo npm run serve


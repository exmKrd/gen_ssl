#!/bin/bash

cd /home/maxime/gen_ssl || exit
source ssl/bin/activate
pip install -r requirement.txt
chmod +x ./main.py
if pgrep -f "/home/maxime/gen_ssl/main.py" > /dev/null
then
    echo "Le script main.py est déjà en cours d'exécution."
else
    echo "Lancement de main.py..."
    ./main.py
fi
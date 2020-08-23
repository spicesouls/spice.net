#!/bin/bash

if which python > /dev/null 2>&1;
then
    :
else
    sudo apt install python3
fi
    
python3 src/client.py

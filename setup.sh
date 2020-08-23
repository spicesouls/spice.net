#!/bin/bash

echo "Installing Client Requirements..."
pip3 install colorama
echo "Client Requirements Installed Successfully!"
echo "Making Scripts executable..."
chmod +x victim.sh
chmod +x connect.sh
echo "Scripts Made Executable Successfully!"
echo ""
echo "To host spicenet on the machine you would like to connect back to, run ./victim.sh"
echo "To connect to a machine hosting spicenet, run ./connect.sh"
echo ""

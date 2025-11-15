#!/bin/bash
# School Work Helper Launcher for Linux/Mac

echo "Starting School Work Helper..."
python3 school_helper.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Failed to start the application."
    echo "Make sure Python 3 is installed and you've run 'pip install -r requirements.txt'"
    echo ""
    read -p "Press enter to continue..."
fi

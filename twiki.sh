#!/bin/bash

echo "Enter search term: "
read query
echo $query
echo "curr dir $(pwd)"

# Define the path to the Python interpreter within the Flatpak bundle
# PYTHON_EXEC=/app/bin/python3

# Run the Python script with the provided arguments
git clone https://github.com/charanravi-online/org.flatpak.twiki.git
cd org.flatpak.twiki.git
python3 twiki.py $query

# python3 twiki.py query
# read query


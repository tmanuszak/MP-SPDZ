#!/bin/bash

# This file will run a GAAP protocol on various MPC protocols and output statistics about each.
# This script takes the follwing arguments:
#   [participants]: This is the number of participants participating in the GAAP
#   [threshold]: At least threshold number of honest participant secret shares are required for a successful authentication
#   [bitsofsecurity]: This is the desired bits of security for the protocol

if [[ $(find . -maxdepth 1 -name '*.x' | wc -c) -eq 0 ]]; then
    Scripts/tldr.sh
fi

python3 generateshares.py $1 $2 $3

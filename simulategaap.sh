#!/bin/bash

# This file will run a GAAP protocol on various MPC protocols and output statistics about each.
# This script takes the follwing arguments:
#   [participants]: This is the number of participants participating in the GAAP
#   [threshold]: At least threshold number of honest participant secret shares are required for a successful authentication
#   [bitsofsecurity]: This is the desired bits of security for the protocol
modprime=(mascot semi lowgear highgear cowgear chaigear hemi temi soho)
mod2k=(spdz2k)
binary=(tiny tinier)

if [[ $(find . -maxdepth 1 -name '*.x' | wc -c) -eq 0 ]]; then
    Scripts/tldr.sh
fi

python3 generateshares.py $1 $2 $3


# BENCHMARKING MOD PRIME MPC PROTOCOLS
# Run the protocol's script on gaap
for mpc in ${modprime[@]}; do
    ./compile.py -F 64 -Z $1 gaap $1 $2 $3
    Scripts/$mpc.sh gaap
done


# BENCHMARKING MOD 2^k MPC PROTOCOLS
# Run the protocol's script on gaap
: '
for mpc in ${mod2k[@]}; do
    echo ${mpc}
done
'


# BENCHMARKING BINARY MPC PROTOCOLS
# Run the protocol's script on gaap
: '
for mpc in ${binary[@]}; do
    echo ${mpc}
done
'

# This python file writes secret share value for participant i to ./Player-Data/Input-Pi-0
# Arguments to this script are [participants] [threshold] [bitsofsecurity]

import os
import sys
import random
import functools
from sympy import nextprime

_PRIME = nextprime(int(sys.argv[3]))  # We will be doing arithmetic in the GF(_PRIME) finite field
_RINT = functools.partial(random.SystemRandom().randint, 0)
_RINTNONZERO = functools.partial(random.SystemRandom().randint, 1)

def inverse(a, prime=_PRIME):
    return pow(a, -1, prime)

def divide(dividend, divisor, prime=_PRIME):
    return (dividend * inverse(divisor)) % prime

def exponentiate(base, power, prime=_PRIME):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return (base * exponentiate(base , power - 1)) % prime

def eval_at(poly, x, prime=_PRIME):
    accum = 0
    for i in range(len(poly)):
        term = exponentiate(x, i)
        accum += (poly[i] * term)
        accum %= prime
    return accum

def make_random_shares(threshold, shares, prime=_PRIME):
    if threshold > shares:
        raise ValueError("Threshold cannot be more than the number of shares.")
    poly = [1] + [_RINT(prime - 1) for i in range(threshold - 2)] + [_RINTNONZERO(prime - 1)]  # secret is always 1 and poly[threshold - 1] must be non-zero
    for i in range(shares):
        os.system("echo " + str(eval_at(poly, i + 1, prime)) + " > Player-Data/Input-P" + str(i) + "-0")
    return

def main():
    numberofparticipants = int(sys.argv[1])
    threshold = int(sys.argv[2])
    bitsofsecurity = int(sys.argv[3])
    make_random_shares(threshold, numberofparticipants)
    return

if __name__ == "__main__":
    main()

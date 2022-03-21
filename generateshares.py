# This python file writes secret share value for participant i to ./Player-Data/Input-Pi-0
# Arguments to this script are [participants] [threshold] [bitsofsecurity]

import os
import random
import functools
from sympy import nextprime

_PRIME = sympy.nextprime(sys.argv[3])  # We will be doing arithmetic in the GF(_PRIME) finite field
_RINT = functools.partial(random.SystemRandom().randint, 0)

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
        return exponentiate((base * base) % prime), power - 1)

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
    poly = [1] + [_RINT(prime - 1) for i in range(threshold - 1)]  # secret is always 1
    for i in range(shares):
        os.system("echo " + eval_at(poly, i + 1, prime) + " > Player-Data/Input-P" + i + "-0")
    return

def main():
    numberofparticipants = sys.argv[1]
    threshold = sys.argv[2]
    bitsofsecurity = sys.argv[3]    

if __name__ == "__main__":
    main()

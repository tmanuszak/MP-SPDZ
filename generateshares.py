# This python file writes secret share value for participant i to ./Player-Data/Input-Pi-0
# Arguments to this script are [numberofparticipants] [threshold] [bitsofsecurity]

import random

def eval_at(poly, x, prime):
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def main():
    numberofparticipants = sys.argv[1]
    threshold = sys.argv[2]
    bitsofsecurity = sys.argv[3]
    poly = [1]  # secret is always 1

    random.seed()

    # poly[1:threshold-1] are random coefficients a_1 ... a_threshold-1
    poly += [random.randint(1, 2**bitsofsecurity - 1) for i in range(threshold - 1)]

    for i in range(numberofparticipants):
        


if __name__ == "__main__":
    main()

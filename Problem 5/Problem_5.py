import os, sys

sys.path.insert(0, 'C:/Users/Alex Marchi/documents/project euler/Functions')

import primes  # a separate python file we made with functions related to primes 
from collections import Counter
from functools import reduce


def main():
    relevant_ints = range(1,21)
    prime_factors = [primes.prime_factors(n) for n in relevant_ints]

    # num_factors: { prime factor : number of occurrences }, e.g. 9 would consist of {3: 2}
    num_factors = {}
    for pf in prime_factors:
        pf_count = Counter(pf)
        for key, value in pf_count.items():
            # check if the num_factors already include this specific prime factorization
            # e.g. the prime factorization of 20 (2,2,5) and 18 (2,3,3) the prime factorization of 12 (2,2,3).
            if key in num_factors:
                if num_factors[key] < value:
                    num_factors[key] = value
            else:
                num_factors[key] = value

    product = 1
    for key, value in num_factors.items():
        product *= (key ** value)

    return product

if __name__=='__main__':
    print(main())

# this guy generates prime numbers
def prime_numbers():
    n = 2
    primes = []
    while True:
        is_prime = True
        for p in primes:
            if p**2 > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n
        n += 1

# as you would imagine, this guy generates primes less than a given number
def primes_less_than(max_prime):
    prime_flags = [True] * max_prime
    prime_flags[0] = prime_flags[1] = False
    for index, flag in enumerate(prime_flags):
        if flag:
            yield index
            for n in range(index**2, max_prime, index):
                prime_flags[n] = False

# here we have the prime factors of n
# it comes as a list, not as a map. 
def prime_factors(n):
    factors = []
    current_factor = 2

    while n > 1:
        while n % current_factor == 0:
            factors.append(current_factor)
            n /= current_factor
        current_factor += 1
        if current_factor ** 2 > n:
            if n > 1:
                factors.append(n)
            break

    return list(map(int, factors))

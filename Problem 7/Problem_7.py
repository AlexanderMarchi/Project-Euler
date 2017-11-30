import math

def prime_sieve(n): # we're going to use the method of the Sieve of Eratosthenes - basic idea is to assume everything is prime, and then remove all multiples of the actual prime numbers.
    p_n = int(2*n*math.log(n)) # over-estimate this guy using p_n ~ n logn
    sieve = [True]*p_n # everything is true
    count = 0
    for i in range(2, p_n):
        if sieve[i]:
            count += 1
            if (count == n):
                return i
            for j in range(2*i,p_n,i): # all multiples of i get set to false
                sieve[j]=False

def main():
    num = 10001
    return prime_sieve(num)

if __name__ == '__main__':
    print(main())
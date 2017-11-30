import math

def prime_sieve(n): # we're going to use the method of the Sieve of Eratosthenes - basic idea is to assume everything is prime, and then remove all multiples of the actual prime numbers.
    sieve = [True]*n # everything is true
    sum = 0
    for i in range(2, n):
        if sieve[i]:
            sum += i
            for j in range(2*i,n,i): # all multiples of i get set to false
                sieve[j]=False

    return sum

def main():
    num = 2000000
    return prime_sieve(num)

if __name__ == '__main__':
    print(main())

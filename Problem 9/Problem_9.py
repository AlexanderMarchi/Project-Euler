# We use Euclid's formula to solve this problem.

from fractions import gcd

def main():
    total = 1000
    i = 0
    while(i**2 < total): 
        i+=1
    max_m = i # here we find the largest i such that m^2 < 1000
    for m in range(max_m):
        for n in range(m): # since m > n > 0
            a = m**2 - n**2 
            b = 2*m*n
            c = m**2 + n**2
            if a+b+c == total:
                return a*b*c

if __name__ == '__main__':
    print(main())
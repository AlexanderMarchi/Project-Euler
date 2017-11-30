from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def main():
    sum_even_fib = 0
    n=0
    while(F(n)<4000000):
        if(round(F(n),0)%2==0): 
            sum_even_fib += round(F(n),0)
        n = n+1
    return sum_even_fib

if __name__ == '__main__':
        print(main())

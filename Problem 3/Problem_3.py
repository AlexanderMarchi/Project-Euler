def main():
    num = 600851475143
    largest_factor = 1
    current_divisor = 1
    while (current_divisor**2 < num): # we know that the largest prime divisor cannot be greater than half the size of our number
        if (num % current_divisor == 0): # if the number is divisible by our current divisor...
            num = num/current_divisor # divide the number accordingly
            largest_factor = current_divisor # and update our "largest factor"
        current_divisor += 1 #increase our current divisor by 1

    if (num>largest_factor):
        largest_factor = num 

    return largest_factor

if __name__ == '__main__':
    print(main())
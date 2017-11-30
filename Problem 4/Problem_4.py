def isPalindrome(s):
    return str(s)==str(s)[::-1] # cool way of comparing a string with it's inverse
    
def main():
    largestPalindrome = 0
    largestx = 0
    largesty = 0

    for x in range(100,999):
        for y in range(100,x+1):
            product = x*y
            if (isPalindrome(product) and product>largestPalindrome):
                largestPalindrome = product
                largestx = x
                largesty = y

    print(largestx) #993
    print(largesty) #913
    return largestPalindrome #906609

if __name__ == '__main__':
    print(main())

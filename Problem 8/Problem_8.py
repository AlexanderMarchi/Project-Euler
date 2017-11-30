def main():
    with open('number.txt','r') as mynum: # read in the string of numbers
        long_int = mynum.read() 

    max_prod = 0
    
    for i in range(len(long_int)-12): #the last 12 will be less than the last 13 by definition so forget about those.
        prod = 1 #need to update the prod for every position in the string
        for j in range(i,i+13): 
           prod *= int(long_int[j]) 
        if prod > max_prod:
           max_prod = prod
            
    return max_prod

if __name__ == '__main__':
    print(main())
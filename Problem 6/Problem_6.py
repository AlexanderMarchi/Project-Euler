def main():
    num = 100
    sum_square = 0
    square_sum = (num*(num+1)/2)**2
    for i in range(1,num+1):
        sum_square += i**2

    return square_sum-sum_square

if __name__ == '__main__':
    print(main())
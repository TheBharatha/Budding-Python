def findDigits(n):
    digits  = list()
    div0 = 0
    for digit in str(n):
        digits.append(int(digit))
    for num in digits:
        if num != 0:
            if n % num == 0:
                div0 += 1
    return(div0)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result) + '\n')

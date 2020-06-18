def print_formatted(number):
    # your code goes here
    space = len(str(bin(number))[2:])
    for value in range(1, number+1):
        print(str(value).rjust(space,' '), str(oct(value))[2:].rjust(space,' '), str(hex(value))[2:].upper().rjust(space,' '), str(bin(value)[2:].rjust(space,' ')))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
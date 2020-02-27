def swap_case(s):
    converted = ''
    for char in s:
        if char.islower():
            converted = converted + char.upper()
        else:
            converted = converted + char.lower()
    return converted

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

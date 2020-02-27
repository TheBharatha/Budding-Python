def split_and_join(line):
    repair = '-'.join(line.split(' '))
    return repair

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

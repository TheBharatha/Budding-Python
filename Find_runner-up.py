if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    i = 1
    runner = True
    while runner:
        m = max(arr) - i
        if m in arr:
            print(m)
            runner = False
        i += 1

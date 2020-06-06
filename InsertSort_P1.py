#!/bin/python3
def insertionSort1(n, arr):
    lastItem = arr[n-1]
    start = n-2
    while lastItem < arr[start] and start >= 0:
        arr[start+1] = arr[start]
        print(*arr)
        start -= 1
    arr[start+1] = lastItem
    print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
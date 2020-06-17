def hourglassSum(arr):
    maxSum = list()
    for row in range(len(arr)-2):
        for col in range(len(arr)-2):
            maxSum.append(sum([arr[row][col], arr[row][col+1], arr[row][col+2], arr[row+1][col+1], arr[row+2][col], arr[row+2][col+1], arr[row+2][col+2]]))
    return(max(maxSum))

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(str(result) + '\n')
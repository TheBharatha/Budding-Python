def utopianTree(n):
    height = list()
    for _ in range(0,n+1):
        if len(height) == 0:
            height.append(1)
        else:
            if height[len(height)-1]%2 != 0:
                height.append(height[len(height)-1] + height[len(height)-1])
            else:
                height.append(height[len(height)-1] + 1)
    return(height[len(height)-1])

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        print(str(result) + '\n')

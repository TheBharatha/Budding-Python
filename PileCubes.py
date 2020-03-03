from collections import deque

if __name__ == "__main__":
    #This deque is used store the popped cube from the original array
    vertical = deque()
    for _ in range(int(input())):
        #Number of cubes
        height = int(input())
        #Side lenght of cubes
        stack = deque(map(int, input().split()))
        #This deque is the original sorted deque used to compare the result
        exm = deque(sorted(stack, reverse=True))
        #Cubes are popped in reference to the max value of the side length
        ind_max = stack.index(max(stack))
        if ind_max == 0 or ind_max == height-1:
            right = height-1
            #Repeat until the original deque goes empty
            while right >= 0:
            #Compare to decide if the cube as to be popped from left or right
                if stack[0] >= stack[right]:
                    vertical.append(stack.popleft())
                else:
                    vertical.append(stack.pop())
                right = len(stack)-1
             #Accordingly display the results
            if vertical == exm:
                print('Yes')
            else:
                print('No')
            stack.clear()
            vertical.clear()  
        else:
            print('No')

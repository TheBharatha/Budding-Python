def jumpingOnClouds(c):
    if len(c) <= 3:
        return 1
    else:
        pointer = 0
        jumps = 0
        while pointer < len(c)-1:
            try:
                if c[pointer + 2] == 0:
                    jumps += 1
                    pointer += 2
                    print('Double ', jumps, 'Pointer ', pointer)
                else:
                    jumps += 1
                    pointer += 1
                    print('Single ', jumps, 'Pointer ', pointer)
            except:
                jumps += 1
                pointer += 2
                print('Last ', jumps, 'Pointer ', pointer)
    return jumps

if __name__ == "__main__":
    a = [0,0,1,0,0,1,0]
    print(jumpingOnClouds(a))
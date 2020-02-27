if __name__ == '__main__':
    test = cmd_list = list()
    command = ''
    N = int(input())
    for _ in range(N):
        command = str(input())
        if 'insert' in command:
            cmd_list.clear()
            cmd_list = list(map(str, command.rstrip().split()))
            test.insert(int(cmd_list[1]),int(cmd_list[2]))
        elif 'print' in command:
            cmd_list.clear()
            print(test)
        elif 'append' in command:
            cmd_list.clear()
            cmd_list = list(map(str, command.rstrip().split()))
            test.append(int(cmd_list[1]))
        elif 'remove' in command:
            cmd_list.clear()
            cmd_list = list(map(str, command.rstrip().split()))
            test.remove(int(cmd_list[1]))
        elif 'pop' in command:
            test.pop()
        elif 'sort' in command:
            test.sort()
        elif 'reverse' in command:
            test.reverse()

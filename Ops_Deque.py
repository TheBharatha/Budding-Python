from collections import deque
if __name__ == '__main__':
    rep = deque()
    lbrace, rbrace = '(', ')'
    for _ in range(int(input())):
        raw_cmd = str(input())
        ops = raw_cmd.rsplit()
        if len(ops) == 1:
            cmd = 'rep.'+ops[0]+lbrace+rbrace
        else:
            cmd = 'rep.'+ops[0]+lbrace+ops[1]+rbrace
        eval(cmd)
    print(*rep)

# 11723
import sys

n = int(sys.stdin.readline().strip())

s = set()

for _ in range(n):

    command = sys.stdin.readline().strip().split()

    if len(command) == 1:
        if command[0] == 'all':
            s = set(range(1,21))

        elif command[0] == 'empty':
            s = set()

    else:
        c, num = command[0], int(command[1])

        if c == 'add':
            s.add(num)

        elif c == 'remove':
            s.discard(num)

        elif c == 'check':
            if num in s:
                print(1)
            else:
                print(0)

        elif c == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)
import sys

input = sys.stdin.readline

f_l = list(map(int, input().split()))

n = f_l[0]

f_l.pop(0)

while len(f_l) < n:
    f_l.extend(map(int, input().split()))

new_l = []

for s in f_l:
    r_s = str(s)[::-1]
    new_l.append(int(r_s))

new_l.sort()

for num in new_l:
    print(num)
import math

s = input()

cnt = [0] * 10

for i in s:
    int_s = int(i)
    cnt[int_s] += 1

temp = math.ceil((cnt[6] + cnt[9]) / 2)
cnt[6] = temp
cnt[9] = temp

print(max(cnt))
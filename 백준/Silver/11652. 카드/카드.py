n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l.sort()

cnt = 1
max_cnt = 1
max_num = l[0]


for j in range(1, n):
    if l[j-1] == l[j]:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
            max_num = l[j-1]
        cnt = 1

if cnt > max_cnt:
    max_cnt = cnt
    max_num = l[-1]
    
print(max_num)
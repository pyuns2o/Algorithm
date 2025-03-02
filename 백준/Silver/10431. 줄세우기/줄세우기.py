# 10431 줄세우기

def Sort(l):
    cnt = 0
    for i in range(len(l) -1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                cnt += 1
    return cnt

n = int(input())

for k in range(n):
    res = list(map(int, input().split()))
    count, people = res[0], res[1:]
    print(count, Sort(people))
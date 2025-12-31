n = int(input())

d = [0] * 1000005

d[1] = 0

for i in range(2, n+1): # n까지 돌게 해야하니까 범위 설정 신경 쓰기.
    d[i] = d[i-1] + 1
    if i%2 == 0: d[i] = min(d[i], d[i//2]+1) # int로 들어가게 // 처리
    if i%3 == 0: d[i] = min(d[i], d[i//3]+1)

print(d[n])
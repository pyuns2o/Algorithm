n, k = map(int, input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

cnt = 0

for c in reversed(coin):
    if k==0:
        break
    cnt += k // c
    k %= c

print(cnt)
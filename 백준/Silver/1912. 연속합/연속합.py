n = int(input())
base = list(map(int, input().split()))


for i in range(1, n):
    base[i] = max(base[i-1] + base[i], base[i])

print(max(base))
n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()

max_weight = 0

for i in range(n):
    weight = ropes[i] * (n-i)
    max_weight = max(max_weight, weight)

print(max_weight)
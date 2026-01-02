from collections import Counter

n, c = map(int, input().split())

base = list(map(int, input().split()))

cnt = Counter(base).most_common()

for a, b in cnt:
    for _ in range(b):
        print(a, end=' ')
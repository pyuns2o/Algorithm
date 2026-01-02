n = int(input())
base = []

for _ in range(n):
    word = input()
    base.append(word)

base = list(set(base))

base.sort(key = lambda x : (len(x), x))

for i in base:
    print(i)
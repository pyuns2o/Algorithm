t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    v = []

    for a in map(int, input().split()):
        v.append((a, 0)) # 0 = A
    
    for b in map(int, input().split()):
        v.append((b, 1)) # 1 = B

    v.sort()

    cnt = 0
    ans = 0

    for value, kind in v:
        if kind == 0: # A
            ans += cnt
        else:
            cnt += 1 # B
    
    print(ans)
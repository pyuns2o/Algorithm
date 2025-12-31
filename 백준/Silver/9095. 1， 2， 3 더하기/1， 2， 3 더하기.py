case = int(input())

def gyeng(n):
    d = [0] * 10000

    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    
    return d[n]

for c in range(case):
    n = int(input())
    print(gyeng(n))
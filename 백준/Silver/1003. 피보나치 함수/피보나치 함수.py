t = int(input())

for _ in range(t):
    n = int(input())

    f_0 = [0] * (n+1)
    f_1 = [0] * (n+1)

    if n >= 0:
        f_0[0] = 1
        f_1[0] = 0

    if n>= 1:
        f_0[1] = 0
        f_1[1] = 1

    if n>1:
        for i in range(2, n+1):
            f_0[i] = f_0[i-1] + f_0[i-2]
            f_1[i] = f_1[i-1] + f_1[i-2]
    
    print(f_0[n], f_1[n])
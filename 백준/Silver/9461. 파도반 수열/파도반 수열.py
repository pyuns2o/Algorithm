t = int(input())

for _ in range(t):
    n = int(input())

    dp = [0] * (n+1)

    if n>= 1 :
        dp[1] = 1
    if n>= 2:
        dp[2] = 1
    if n>= 3:
        dp[3] = 1
    if n>= 4:
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2]
    
    print(dp[n])
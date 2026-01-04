n = int(input())
su = list(map(int, input().split()))
dp = [0] * n



for i in range(n):
    dp[i] = su[i]
    for j in range(i):
        if su[j] < su[i]:
            dp[i] = max(dp[i], dp[j] + su[i])

print(max(dp))
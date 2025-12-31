n = int(input())

step = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    step[i] = int(input())

dp[1] = step[1]
if n>1 : dp[2] = step[1] + step[2]
if n>2 : dp[3] = step[3] + max(step[1], step[2])

for i in range(4, n+1):
    dp[i] = step[i] + max(dp[i-2], dp[i-3] + step[i-1])

print(dp[n])
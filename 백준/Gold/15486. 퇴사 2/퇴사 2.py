import sys
input = sys.stdin.readline

n = int(input())

T = [0] * (n + 1)
P = [0] * (n + 1)

for i in range(1, n + 1):
    T[i], P[i] = map(int, input().split())

# dp[i] = i번째 날부터 얻을 수 있는 최대 수익
dp = [0] * (n + 2)

for i in range(n, 0, -1):
    # 상담을 할 수 없는 경우
    if i + T[i] > n + 1:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(
            dp[i + 1],           # 상담 안 함
            P[i] + dp[i + T[i]]  # 상담 함
        )

print(dp[1])
def solution(m, n, puddles):
    MOD = 1000000007
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    dp[1][1] = 1 # 시작점
    
    puddles_set = {(x,y) for x,y in puddles}
    
    for x in range(1, m+1):
        for y in range(1, n+1):
            
            if (x,y) in puddles_set:
                dp[x][y] = 0 # 웅덩이 0으로 설정
            
            elif not (x==1 and y==1): #시작점 아닌 경우만 넣도록
                from_left = dp[x-1][y] if x > 1 else 0 # 현재 위치에서 왼쪽 값
                from_top = dp[x][y-1] if y > 1 else 0 # 현재 위치에서 위쪽 값
                dp[x][y] = (from_left + from_top) % MOD
    
    return dp[m][n]
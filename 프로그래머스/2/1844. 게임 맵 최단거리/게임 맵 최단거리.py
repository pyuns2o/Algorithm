from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)] # 방문 여부 초기화
    
    dx = [0,0,-1,1] # 좌, 우
    dy = [-1,1,0,0] # 상, 하
    
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue # 맵 범위 밖이면 무시
            
            if maps[nx][ny] == 0 or visited[nx][ny] != 0: #벽인 경우와 이미 방문한 경우 패스
                continue
                
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    return visited[n-1][m-1] if visited[n-1][m-1] != 0 else -1
    
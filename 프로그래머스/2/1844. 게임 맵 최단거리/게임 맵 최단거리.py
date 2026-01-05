from collections import deque

def solution(maps):
    n = len(maps) # 세로 길이
    m = len(maps[0]) # 가로 길이
    dist = [[-1] * m for _ in range(n)] # 거리 배열 초기화
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque()
    q.append((0,0))
    dist[0][0] = 1
    
    while q:
        cur_x, cur_y = q.popleft()
        
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]
            
            if nx>= n or nx<0 or ny >= m or ny <0:
                continue
                
            if maps[nx][ny] == 0 or dist[nx][ny] != -1:
                continue
            
            q.append((nx,ny))
            dist[nx][ny] = dist[cur_x][cur_y] + 1

    return dist[n-1][m-1]
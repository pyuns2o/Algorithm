from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dist = [[0]*m for _ in range(n)]

dx = [-1, 0 , 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque()
    q.append((0,0))
    dist[0][0] = 1

    while q:
        cur_x, cur_y = q.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue

            if board[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[cur_x][cur_y] + 1
                q.append((nx,ny))
    
    return dist[n-1][m-1]

print(bfs())
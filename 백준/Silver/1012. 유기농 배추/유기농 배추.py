from collections import deque

T = int(input())

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    size = 1
    
    while q:
        cur_x, cur_y = q.popleft()
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx<0 or nx >= N or ny<0 or ny>= M:
                continue

            if visited[nx][ny] or board[nx][ny] != 1:
                continue

            visited[nx][ny] = True
            q.append((nx,ny))
            size += 1

    return size

for _ in range(T):

    N, M, K = map(int, input().split())

    board = [[0]*M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    count = 0
    max_size = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and board[i][j] == 1:
                cur_size = bfs(i,j)
                count += 1
                max_size = max(max_size, cur_size)
    print(count)
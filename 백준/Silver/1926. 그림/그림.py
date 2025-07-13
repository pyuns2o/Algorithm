from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_size = []
num = 0

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
        

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue

            if visited[nx][ny] or board[nx][ny] == 0:
                continue
            
            visited[nx][ny] = True
            q.append((nx,ny))
            size += 1

    return size

count = 0 # 그림수
max_size = 0 # 가장 큰 그림 크기

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and board[i][j] == 1:
            cur_size = bfs(i, j)
            count += 1
            max_size = max(max_size, cur_size)

print(count)
print(max_size)
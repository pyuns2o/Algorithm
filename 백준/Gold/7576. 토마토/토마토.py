from collections import deque

#### board에서
# 익은 토마토 1
# 안 익은 토마토 0
# 토마토 없는 칸 -1

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i,j))
            dist[i][j] = 0

while q:
    cur_x, cur_y = q.popleft()

    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        if nx<0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] == 0 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

answer = 0
flag = False

for i in range(n):
    for j in range(m):
        if board[i][j] ==0 and dist[i][j] == -1:
            flag = True
        answer = max(answer, dist[i][j])

if flag == True:
    print(-1)
else:
    print(answer)
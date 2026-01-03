from collections import deque

m,n,h = map(int, input().split())

board = []
dist = []

for z in range(h):
    layer = []
    d_layer = []
    for y in range(n):
        layer.append(list(map(int, input().split())))
        d_layer.append([-1] * m)
    board.append(layer)
    dist.append(d_layer)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

# 모든 익은 토마토 시작점으로 넣기
for z in range(h):
    for y in range(n):
        for x in range(m):
            if board[z][y][x] == 1:
                q.append((z,y,x))
                dist[z][y][x] = 0

while q:
    cur_z, cur_y, cur_x = q.popleft()

    for dir in range(6):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]
        nz = cur_z + dz[dir]

        if nx >= m or nx < 0 or ny >= n or ny <0 or nz >= h or nz<0:
            continue

        if board[nz][ny][nx] == 0 and dist[nz][ny][nx] == -1:
            dist[nz][ny][nx] = dist[cur_z][cur_y][cur_x] + 1
            q.append((nz, ny, nx))
ans = 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            if board[z][y][x] == 0 and dist[z][y][x] == -1:
                print(-1)
                exit()
            ans = max(ans, dist[z][y][x])

print(ans)
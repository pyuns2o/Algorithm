from collections import deque

n = int(input())

board = []
e_board = [] # R G를 R로 통일해서 집어넣기?

visited = [[0]*n for _ in range(n)]
e_visited = [[0]*n for _ in range(n)]

for _ in range(n):
    row = list(input().strip())

    board.append(row)
    e_board.append(['R' if c=='G' else c for c in row])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,b,vis):
    q = deque()
    q.append((x,y))
    vis[x][y] = True

    while q:
        cur_x, cur_y = q.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if vis[nx][ny] or b[nx][ny] != b[cur_x][cur_y]:
                continue

            q.append((nx,ny))
            vis[nx][ny] = True
count = 0
e_count = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j,board, visited)
            count += 1

for i in range(n):
    for j in range(n):
        if e_visited[i][j] == False:
            bfs(i,j,e_board, e_visited)
            e_count += 1

print(count, e_count, end='')
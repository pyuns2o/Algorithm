# 지훈이와 불에 대해 각각 bfs
# 지훈이 도달 시간이 불 도달 시간보다 크면 갈 수 없는 곳이기 때문에 벽처럼 처리하면 됨.
# 불 시간, 지훈이 시간 따로따로 기록하면 됨.

from collections import deque
r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]

fire = [[-1]*c for _ in range(r)]
jihun = [[-1]*c for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

j_q = deque()
f_q = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            j_q.append((i,j))
            jihun[i][j] = 1
        elif board[i][j] == 'F':
            f_q.append((i,j))
            fire[i][j] = 1

# 불 bfs 기록
while f_q:
    f_x, f_y = f_q.popleft()

    for dir in range(4):
        nx = f_x + dx[dir]
        ny = f_y + dy[dir]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if board[nx][ny] == '#' or fire[nx][ny] != -1:
            continue

        fire[nx][ny] = fire[f_x][f_y] + 1
        f_q.append((nx,ny))

# 지훈이 bfs 기록
while j_q:
    j_x, j_y = j_q.popleft()

    for dir in range(4):
        nx = j_x + dx[dir]
        ny = j_y + dy[dir]
        next_time = jihun[j_x][j_y] + 1

        if nx < 0 or nx >= r or ny <0 or ny >= c: # 가장자리 도착
            print(jihun[j_x][j_y])
            exit()

        if board[nx][ny] == '#' or jihun[nx][ny] != -1:
            continue
        # 지훈이 값이 더 작은 경우 이동 가능, 불이 아직 오지도 않은 상태면 이동 가능
        if next_time >= fire[nx][ny] and fire[nx][ny] != -1:
            continue

        jihun[nx][ny] = next_time
        j_q.append((nx,ny))

print("IMPOSSIBLE")
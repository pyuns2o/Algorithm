from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(h)]

    fire = [[-1]*w for _ in range(h)]
    person = [[-1]*w for _ in range(h)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    f_q = deque()
    p_q = deque()

    skip = False

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                # 🔥 시작부터 탈출 가능
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    print(1)
                    skip = True
                p_q.append((i,j))
                person[i][j] = 0
            elif board[i][j] == '*':
                f_q.append((i,j))
                fire[i][j] = 0

    if skip:
        continue

    # 불 bfs 처리
    while f_q:
        f_x, f_y = f_q.popleft()

        for dir in range(4):
            nx = f_x + dx[dir]
            ny = f_y + dy[dir]

            if nx >= h or nx<0 or ny>=w or ny<0:
                continue

            if board[nx][ny] == '#' or fire[nx][ny] != -1:
                continue

            fire[nx][ny] = fire[f_x][f_y] + 1
            f_q.append((nx, ny))
    
    escape = False

    # 사람 기록
    while p_q:
        p_x, p_y = p_q.popleft()

        for dir in range(4):
            nx = p_x + dx[dir]
            ny = p_y + dy[dir]
            p_time = person[p_x][p_y] + 1

            if nx >= h or nx<0 or ny>=w or ny<0:
                print(p_time)
                escape = True
                break

            if board[nx][ny] == '#':
                continue

            if person[nx][ny] != -1:
                continue

            if p_time >= fire[nx][ny] and fire[nx][ny] != -1:
                continue

            person[nx][ny] = p_time
            p_q.append((nx,ny))
        
        if escape:
            break

    if escape == False:
        print("IMPOSSIBLE")
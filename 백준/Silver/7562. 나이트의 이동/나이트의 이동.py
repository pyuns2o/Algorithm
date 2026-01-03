from collections import deque

t = int(input())

dx = [1,-1,1,-1,2,-2,2,-2]
dy = [2,2,-2,-2,1,1,-1,-1]

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())

    dist = [[0]*l for _ in range(l)]

    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0

    while q:
        cur_x, cur_y = q.popleft()

        if cur_x == gx and cur_y == gy:
            print(dist[cur_x][cur_y])
            break

        for dir in range(8):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx >= l or nx<0 or ny>= l or ny <0:
                continue

            if dist[nx][ny] == 0:
                dist[nx][ny] = dist[cur_x][cur_y] + 1
                q.append((nx,ny)) # 큐에 다시 넣어줘야 한다!!
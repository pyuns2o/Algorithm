from collections import deque
import sys
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

t = int(input())
out = []

for _ in range(t):
    w, h = map(int, input().split())
    board = [input().rstrip() for _ in range(h)]  # 문자열로 유지(더 빠름)

    fire = [[-1] * w for _ in range(h)]
    person = [[-1] * w for _ in range(h)]

    f_q = deque()
    p_q = deque()

    # 시작점 수집
    for i in range(h):
        row = board[i]
        for j, ch in enumerate(row):
            if ch == '*':
                fire[i][j] = 0
                f_q.append((i, j))
            elif ch == '@':
                person[i][j] = 0
                p_q.append((i, j))

    # 불 BFS
    while f_q:
        x, y = f_q.popleft()
        nt = fire[x][y] + 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if fire[nx][ny] != -1:
                    continue
                if board[nx][ny] == '#':
                    continue
                fire[nx][ny] = nt
                f_q.append((nx, ny))

    # 사람 BFS
    escaped = False
    while p_q and not escaped:
        x, y = p_q.popleft()
        nt = person[x][y] + 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 탈출: 맵 밖으로 나가면 성공
            if not (0 <= nx < h and 0 <= ny < w):
                out.append(str(nt))
                escaped = True
                break

            if person[nx][ny] != -1:
                continue
            if board[nx][ny] == '#':
                continue

            ft = fire[nx][ny]
            if ft != -1 and nt >= ft:
                continue

            person[nx][ny] = nt
            p_q.append((nx, ny))

    if not escaped:
        out.append("IMPOSSIBLE")

print("\n".join(out))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

DIRS = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}

def watch(board, x, y, direction):
    changed = []
    nx, ny = x, y

    while True:
        nx += dx[direction]
        ny += dy[direction]

        if not (0 <= nx < N and 0 <= ny < M):
            break

        if board[nx][ny] == 6:
            break

        if board[nx][ny] == 0:
            board[nx][ny] = -1
            changed.append((nx, ny))

    return changed

def dfs(idx):
    global answer

    if idx == len(cctvs):
        blind = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    blind += 1
        answer = min(answer, blind)
        return

    x,y,t = cctvs[idx]

    for dir in DIRS[t]:
        changed_all = []
        for d in dir:
            changed_all.extend(watch(board,x,y,d))
    
        dfs(idx + 1)

        for r,c in changed_all:
            board[r][c] = 0

N,M = map(int, input().split())
board = []
cctvs = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((i,j,row[j]))

answer = 10**9
dfs(0)
print(answer)
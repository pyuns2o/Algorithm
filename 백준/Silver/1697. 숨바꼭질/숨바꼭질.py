# +1, -1, *2를 순회하면서 방문거리를 표시한다고 생각하면 되는거임

from collections import deque


n, k = map(int, input().split())
limit = 100002
dist = [-1] * limit
q = deque()

dist[n] = 0
q.append(n)

while q:
    cur_x = q.popleft()

    if cur_x == k:
        print(dist[cur_x])
        exit()

    for nx in [cur_x + 1, cur_x -1, cur_x *2]:
        if nx <0 or nx >= limit:
            continue

        if dist[nx] != -1:
            continue

        dist[nx] = dist[cur_x] + 1
        q.append(nx)
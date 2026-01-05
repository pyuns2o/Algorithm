from collections import deque
# dist 행렬을 만들어서 거리를 다 저장한 다음에 max(dist)의 개수를 count하면 될 것으로 생각됨.

def solution(n, edge):
    # 인접 리스트 만들어주기
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n+1)
    dist[1] = 0
    
    q = deque()
    q.append(1)
    
    while q:
        curr = q.popleft()
        for nxt in graph[curr]: # 인접리스트 연결된 애들 돌아
            # 방문한 적 없다면
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                q.append(nxt)
    
    max_dist = max(dist[1:])
    answer = dist.count(max_dist)
    
    return answer
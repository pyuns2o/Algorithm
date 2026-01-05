from collections import deque

def bfs(start, computers, visited, n):
    q = deque()
    # 시작점 방문 처리 및 큐에 집어넣기
    q.append(start)
    visited[start] = True
    
    while q:
        curr = q.popleft()
        
        for next in range(n):
            # 컴퓨터끼리 네트워크 연결되어 있고 방문 안 한 경우
            if computers[curr][next] == 1 and visited[next] == False:
                visited[next] = True
                q.append(next)
            
def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        # 전체 컴퓨터를 돌면서 새로운 네트워크를 찾을 때 (bfs가 돌 때마다 count 되도록 설정.)
        if visited[i] == False:
            count += 1
            bfs(i, computers, visited, n)
        
    return count
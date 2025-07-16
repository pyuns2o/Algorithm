from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1 # 시작 노드 카운트 포함
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1 # 연결된 송전탑 수 증가
    return count

def solution(n, wires):
    min_diff = float('inf')
    
    for i in range(len(wires)):
        # 전선 하나 끊기 -> i번째 전선 제외한 나머지로 그래프 생성
        temp_wires = wires[:i] + wires[i+1:]
        
        graph = [[] for _ in range(n+1)]
        for a, b in temp_wires:
            graph[a].append(b)
            graph[b].append(a)
            
        visited = [False] * (n+1)
        # 한 덩어리 세기
        count = bfs(1, graph, visited)
        # 나머지 덩어리는 전체에서 한덩어리 수를 빼면 됨
        other = n - count
        
        min_diff = min(min_diff, abs(count - other))
        
    return min_diff
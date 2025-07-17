def solution(n, costs):
    # 비용 기준 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    # 각 노드 부모 자기 자신으로 설정
    parent = [i for i in range(n)]
    # 부모 찾기
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    # 노드 연결(부모 연결)
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b: # 연결 안되어 있으면
            parent[root_b] = root_a # 부모로 연결
            return True # 연결
        return False # 이미 연결시 False
    
    answer = 0
    
    for a, b, cost in costs:
        if union(a,b):
            answer += cost
    
    return answer
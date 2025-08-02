def solution(tickets):
    n = len(tickets)
    tickets.sort()  # 알파벳 순으로 정렬
    
    visited = [False] * n 
    answer = []             

    def dfs(current, path, used):
        # 모든 티켓 사용시 종료
        if used == n:
            answer.extend(path)   # 현재 경로를 answer에 넣기
            return True           # True 반환해서 재귀 종료
        
        for i in range(n):
            # 방문 안했고 현재 위치에서 출발하는 티켓이라면
            if not visited[i] and tickets[i][0] == current: 
                visited[i] = True # 티켓 사용
                # 다음으로 넘어가서 다시 재귀
                if dfs(tickets[i][1], path + [tickets[i][1]], used + 1):
                    return True                       
                visited[i] = False # 실패시 백트래킹 (원상복구)
        
        return False

    dfs("ICN", ["ICN"], 0)
    return answer
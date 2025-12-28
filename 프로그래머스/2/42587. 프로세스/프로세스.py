from collections import deque

def solution(priorities, location):
    queue = deque((i,p) for i,p in enumerate(priorities))
    answer = 0
    
    while queue:
        max_p = max(p for (_, p) in queue) #리스트 컴프리헨션!!!
        
        curr = queue.popleft()
        
        if curr[1] < max_p:
            queue.append(curr)
                         
        else:
            answer += 1
            if curr[0] == location:
                return answer
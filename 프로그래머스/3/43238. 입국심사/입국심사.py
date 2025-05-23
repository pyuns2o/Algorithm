def solution(n, times):
    left = 1
    right = max(times) * n # 제일 늦게되는 시간 계산
    
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        total = sum(mid // time for time in times)
        
        if total >= n:
            answer = mid
            right = mid - 1 # 시간 줄여보기
        else:
            left = mid + 1 # 시간 늘려보기
            
    return answer
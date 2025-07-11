def solution(people, limit):
    people.sort()
    left = 0 # 왼쪽 제일 끝 인덱스
    right = len(people) -1 # 오른쪽 제일 끝
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        # limit 초과시 무거운 사람을 무조건 태우기    
        right -= 1
        answer += 1
            
    return answer
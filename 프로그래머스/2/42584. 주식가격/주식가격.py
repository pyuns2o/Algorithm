def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i, price in enumerate(prices):
        # 가격이 떨어졌다면
        while stack and price < prices[stack[-1]]:
            prev_i = stack.pop()
            answer[prev_i] = i - prev_i # 지금 시점 - 이전 시점 = 버틴 시간
            
        # 떨어지지 않은 경우 스택에 넣어주기
        stack.append(i)
    
    # 끝까지 떨어지지 않고 스택에 쌓여있는 애들 처리
    for i in stack:
        answer[i] = n - 1 - i # 마지막 index - 현재 index
        
        
    return answer
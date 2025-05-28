def solution(number, k):
    # k개 만큼 채우면 끝내고
    # 차례대로 넣고 더 큰 값이면 그걸로 채우고 쭉쭉
    stack = []
    
    for digit in number:
        while k > 0 and stack and stack[-1] < digit: # 아직 k가 남아있고 stack 비어있지 않고 맨 마지막 숫자보다 현재 digit이 더 크다면
            stack.pop() # 마지막 꺼 지우고
            k -= 1 # k 차감하고
        stack.append(digit) # digit을 집어넣어
    # 다 돌았는데도 k가 남아있으면
    if k > 0:
        stack = stack[:-k] # 뒤에서 더 지우기

    return ''.join(stack)
def solution(numbers, target):
    answer = 0
    def dfs(idx, summ):
        nonlocal answer
        if idx == len(numbers):
            if summ == target:
                answer += 1
            return
        dfs(idx+1, summ + numbers[idx])
        dfs(idx+1, summ - numbers[idx])
    dfs(0,0)
    return answer
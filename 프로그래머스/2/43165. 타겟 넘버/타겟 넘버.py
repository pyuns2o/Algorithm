def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        p = dfs(index + 1, current_sum + numbers[index])
        m = dfs(index + 1, current_sum - numbers[index])
        return p + m
    return dfs(0,0)
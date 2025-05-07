def solution(nums):
    uniq_list = list(set(nums))
    answer = min(len(nums) // 2, len(uniq_list))
    return answer
def solution(nums):
    base_len = len(nums)/2
    uni_nums = set(nums)
    uni_len = len(uni_nums)
    return min(base_len, uni_len)
import math

def solution(n):
    n_sq = math.sqrt(n)
    # answer = (n_sq + 1) ** 2
    if n_sq == int(n_sq):
        return (n_sq + 1) ** 2
    else:
        return -1
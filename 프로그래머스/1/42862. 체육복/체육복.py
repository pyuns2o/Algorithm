def solution(n, lost, reserve):
    # 겹치는 사람 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    # 빌려주기
    for s in sorted(lost_set):
        if s - 1 in reserve_set:
            reserve_set.remove(s-1)
        elif s + 1 in reserve_set:
            reserve_set.remove(s+1)
        else:
            n -= 1 # 체육복 못 빌림
    return n
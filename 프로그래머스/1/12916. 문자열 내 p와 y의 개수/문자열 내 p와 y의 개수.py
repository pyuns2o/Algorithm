def solution(s):
    s = s.upper()
    p_cnt = 0
    y_cnt = 0
    
    for c in s:
        if c == 'P':
            p_cnt += 1
        elif c == 'Y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False
        
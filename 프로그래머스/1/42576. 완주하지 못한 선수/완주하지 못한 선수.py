from collections import Counter

def solution(participant, completion):
    answer = ''
    c_par = Counter(participant)
    c_com = Counter(completion)
    
    for p_name in c_par:
        if c_par[p_name] != c_com[p_name]:
            answer = p_name
    return answer
from collections import Counter

def solution(clothes):
    type_counter = Counter([kind for name, kind in clothes])
    
    answer = 1
    
    for count in type_counter.values():
        answer *= (count + 1)
        
    return answer - 1
from collections import Counter

def make_2set(s):
    result = []
    s = s.lower()
    
    for i in range(len(s)-1):
        pair = s[i:i+2]
        
        if pair.isalpha():
            result.append(pair)
            
    return result

def solution(str1, str2):
    l_1 = make_2set(str1)
    l_2 = make_2set(str2)
    
    cnt_1 = Counter(l_1)
    cnt_2 = Counter(l_2)
    
    gyo = cnt_1 & cnt_2
    hap = cnt_1 | cnt_2
    
    gyo_cnt = sum(gyo.values())
    hap_cnt = sum(hap.values())
    
    if hap_cnt == 0:
        return 65536
    else:
        return int((gyo_cnt / hap_cnt) * 65536)
def solution(s):
    answer = []
    s = s[2:-2]
    s_l = s.split('},{')
    s_l.sort(key=lambda x: len(x))
    
    for i in s_l:
        numbers = list(map(int, i.split(',')))
        for num in numbers:
            if num not in answer:
                answer.append(num)
    return answer
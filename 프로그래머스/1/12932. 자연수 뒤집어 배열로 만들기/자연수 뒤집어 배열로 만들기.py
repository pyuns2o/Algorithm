def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)-1, -1, -1):
        int_n = int(n[i])
        answer.append(int_n)
        
    return answer
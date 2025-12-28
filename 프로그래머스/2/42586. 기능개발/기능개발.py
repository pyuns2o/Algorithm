import math

def solution(progresses, speeds):
    temp = []
    answer = []
    for i in range(len(progresses)):
        temp.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    st = temp[0]
    
    for j in range(len(temp)):
        if j == 0:
            count = 1
            continue
            
        elif st >= temp[j]:
            count += 1
        
        elif st < temp[j]:
            answer.append(count)
            count = 1
            st = temp[j]
            
    answer.append(count)
    
    return answer
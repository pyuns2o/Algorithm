def solution(x):
    summ = 0
    str_x = str(x)
    
    for i in range(len(str_x)):
        summ += int(str_x[i])
        
    if x % summ == 0:
        return True
    else:
        return False
def num_convert(absolute_num, sign):
    if sign == True:
        return absolute_num
    else:
        return absolute_num * -1
    
def solution(absolutes, signs):
    total_sum = 0
    for i in range(len(absolutes)):
        actual_num = num_convert(absolutes[i], signs[i])
        total_sum += actual_num
    return total_sum
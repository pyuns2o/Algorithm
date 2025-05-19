def solution(array, commands):
    answer = []
    for m in range(len(commands)):
        i = commands[m][0]
        j = commands[m][1]
        k = commands[m][2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer
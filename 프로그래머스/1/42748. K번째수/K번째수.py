def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i,j,k = commands[n][:]
        tmp = array[i-1:j]
        tmp.sort()
        ans = tmp[k-1]
        answer.append(ans)
    return answer
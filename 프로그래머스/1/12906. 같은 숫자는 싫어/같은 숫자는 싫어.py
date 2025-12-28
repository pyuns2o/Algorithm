# 아하 그냥 중복을 제거하면 되는 문제가 아니구나
# 연속일 경우!!

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
    return answer
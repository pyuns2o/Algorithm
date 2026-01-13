def solution(num):
    cnt = 0
    while num != 1:
        # 짝수라면
        if num % 2 == 0:
            num = num//2
            cnt += 1
        # 홀수라면
        else:
            num = num*3 + 1
            cnt += 1
        # cnt 500 넘으면
        if cnt >= 500:
            return -1
    return cnt
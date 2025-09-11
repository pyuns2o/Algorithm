# 연속된 수 = 1씩 늘어나는 숫자들로 구성되있는 거잖아
# a, a+1, a+2, ... d = 1, a1 = a 등차수열의 합?
# 등차수열의 합 공식 머드라.. r{2a + (r-1)} / 2 = n -> a값이 int면 개수 +? for문 길이는 어캐? 복잡하다 이건
# n만큼 돌리면서 연속으로 쭉 더해가면서 되면 += 1 하고, 더한 값이 n 넘어가면 나가게 구현
def solution(n):
    answer = 0
    for i in range(1 , n+1):
        curr_sum = 0
        for j in range(i,n+1):
            curr_sum += j
            if curr_sum == n:
                answer += 1
                break
            elif curr_sum > n:
                break
    return answer
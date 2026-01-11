def solution(n):
    str_n = str(n)
    ans = []
    for s in str_n:
        ans.append(s)
    ans.sort(reverse = True)
    s_ans = "".join(ans)
    return int(s_ans)
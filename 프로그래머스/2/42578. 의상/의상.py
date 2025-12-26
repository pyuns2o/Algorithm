from collections import Counter

def solution(clothes):
    answer = 1
    c_list = []
    # 의상종류만 담긴 리스트를 새로 파
    for item in clothes:
        c_list.append(item[1])
    # counter로 의상 종류별로 갯수를 세
    clo_count = Counter(c_list)
    # 개수 + 1씩 곱해 (안 입는 경우의 수가 있는거니까)
    for cnt in clo_count.values():
        answer = answer * (cnt+1)
    # 그다음에 안 입는 경우는 없으니까 -1 해줘
    return answer -1
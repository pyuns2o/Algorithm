# h 이상 인용된 논문이 h편이 있는가?
def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if c < i + 1: # h값이 인용된 논문의 수보다 작은 경우 끝나도록
            return i
    return len(citations) # 끝까지 h 값 만족하면 전체 개수를 반환하도록
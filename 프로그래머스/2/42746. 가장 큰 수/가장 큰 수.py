# 우선 문자열로 만들고
# 그냥 문자열 정렬은 아닐거고
# 우으으으음 후아아앙와오아

def solution(numbers):
    # 문자열로 만들어주기
    numbers = list(map(str, numbers))
    # 1000 제외하면 최대 3자리, 2개 붙이면 최대 6자리
    numbers.sort(key=lambda x: x*3, reverse= True)
    
    return '0' if numbers[0] == '0' else ''.join(numbers)
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]): # 바로 옆옆만 비교할 수 있는 코드잖아...
            return False
    return answer
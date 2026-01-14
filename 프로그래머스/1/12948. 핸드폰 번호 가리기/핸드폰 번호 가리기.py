def solution(phone_number):
    tmp = []
    phone_lenght = len(phone_number)
    for i in range(phone_lenght):
        if i < phone_lenght-4:
            tmp.append('*')
        else:
            tmp.append(phone_number[i])
        
    return ''.join(tmp)
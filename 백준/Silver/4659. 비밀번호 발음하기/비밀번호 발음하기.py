#4659 비밀번호 발음하기

def is_acceptable(password):
    mo = 'aeiou'
    
    if not any(c in mo for c in password):
        return f"<{password}> is not acceptable."

    for i in range(len(password)):
        if i>=2 and (password[i] in mo) == (password[i-1] in mo) == (password[i-2] in mo):
            return f"<{password}> is not acceptable."
        
        if i >=1 and password[i] == password[i-1] and password[i] not in "eo":
            return f"<{password}> is not acceptable."
    
    return f"<{password}> is acceptable."

while True:
    password = input().strip()
    if password == "end":
        break
    print(is_acceptable(password))
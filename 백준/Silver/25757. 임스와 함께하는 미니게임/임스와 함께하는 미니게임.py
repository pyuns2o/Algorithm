# 25757 임스와 함께하는 미니게임

n, game = input().split()
n = int(n)

user_list = []

for _ in range(n):
    user = input()
    user_list.append(user)

uniq_user = list(set(user_list))

if game == 'Y':
    print(len(uniq_user))
elif game == 'F':
    print(len(uniq_user)//2)
elif game == 'O':
    print(len(uniq_user)//3)
# 2816
n = int(input())

channel_list = []

for i in range(n):
    channel = input()
    if channel == 'KBS1':
        idx1 = i
    elif channel == 'KBS2':
        idx2 = i
    channel_list.append(channel)

if idx1 > idx2:
    idx2 +=1

print('1'*idx1 + '4'* idx1 + '1'*idx2 + '4'*(idx2-1))
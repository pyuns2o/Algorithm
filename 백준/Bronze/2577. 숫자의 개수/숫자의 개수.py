tot = 1
num = [0] * 10

for i in range(3):
    temp = int(input())
    tot = tot * temp

for s in str(tot):
    int_s = int(s)
    num[int_s] += 1

for i in range(10):
    print(num[i])
n = int(input()) #기타의 개수
l = []

def sum_num(inputs):
    summ = 0
    for i in inputs:
        if i.isdigit():
            summ += int(i)
    return summ

for _ in range(n):
    t = input()
    l.append(t)

l.sort(key = lambda x : (len(x), sum_num(x), x))

for i in range(len(l)):
    print(l[i])
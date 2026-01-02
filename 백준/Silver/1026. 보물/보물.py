# 당연하게도 B는 고정이니까 음
# B가 큰건 A가 작은걸 넣을 수 있도록 정렬해서 곱해주면 되는거 아닌가?

# 0 1 1 1 6
# 8 7 3 2 1

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort(reverse = True)
a.sort()

tot = 0

for i in range(n):
    tot += a[i] * b[i]

print(tot)
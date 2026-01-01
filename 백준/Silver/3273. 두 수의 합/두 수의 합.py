base = [0] * 2000005

n = int(input())

input_list = list(map(int, input().split()))

x = int(input())

cnt = 0

# for문으로 감싸서 처리를 하면 될텐뎅
for num in input_list:
    if base[x - num] > 0:
        cnt += 1
        base[num] += 1
    else:
        base[num] += 1

print(cnt)
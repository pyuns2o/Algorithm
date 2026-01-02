n = int(input())

schedule = []

for _  in range(n):
    s, f = map(int, input().split())
    schedule.append((s, f))

# 끝나는 시간 기준으로 정렬, 끝나는 시간이 같은 경우 시작 시간이 빠른 걸 기준으로 정렬하도록
schedule.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for start, end in schedule:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)
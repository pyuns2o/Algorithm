import sys
from itertools import combinations

N, M = map(int, input().split())

houses = [] # 집 좌표 저장
chickens = [] # 치킨 집 좌표 저장

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            houses.append((r,c))
        elif row[c] == 2:
            chickens.append((r,c))

answer = float('inf') # 정답 초기화

for select in combinations(chickens, M):

    city_dist = 0 # 현재 치킨 집 조합에서

    for hx, hy in houses: #각 집마다
        # 가장 가까운 치킨집 거리를 구한다.
        min_dist = float('inf')

        for cx, cy in select:
            dist = abs(hx - cx) + abs(hy - cy)
            if dist < min_dist:
                min_dist = dist
        
        #현재 조합에서의 치킨 거리
        city_dist += min_dist

    if city_dist < answer:
            answer = city_dist

print(answer)
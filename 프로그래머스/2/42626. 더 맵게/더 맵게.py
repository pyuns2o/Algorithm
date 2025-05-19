# def solution(scoville, K):
#     count = 0

#     while True:
#         scoville.sort()

#         if scoville[0] >= K:
#             return count

#         if len(scoville) < 2:
#             return -1

#         # 앞 두 개 섞기
#         first = scoville.pop(0)
#         second = scoville.pop(0)
#         new_food = first + second * 2

#         scoville.append(new_food)
#         count += 1

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K :
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_sco = first + (second * 2)
        heapq.heappush(scoville, new_sco)
        
        count += 1
    
    return count

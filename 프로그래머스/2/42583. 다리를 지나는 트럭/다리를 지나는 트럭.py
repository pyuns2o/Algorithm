from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length) # 다리 생성 및 초기화
    total_weight = 0 # 다리 위 무게 합
    
    truck_weights = deque(truck_weights)
    
    while bridge:
        time += 1
        left = bridge.popleft() # 맨앞 원소 빼내기
        total_weight -= left #무게 빼기
        
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
                
    return time
    
    
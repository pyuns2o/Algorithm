def solution(name):
    # 위, 아래로 가는 것 중 최적 pick
    # 왼쪽, 오른쪽 가는 것 중 최적 pick 해서 더하기
    
    answer = 0
    
    for ch in name:
        answer += min(ord(ch) - ord("A"), ord("Z") - ord(ch) + 1)
        
    move = len(name) - 1 # 1) 그냥 오른쪽으로 쭉 갈 경우
    
    # ex. "ABAAABA" 라고 생각해보기..
    
    for i in range(len(name)):
        next_i = i + 1
        # 연속된 A가 있다면 쭉쭉 넘기기
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        # 2) 오른쪽으로 먼저 갔다가 뒤로 돌아오기
        move_r = (i * 2) + (len(name) - next_i)
        # 3) 뒤로(왼쪽)으로 먼저 갔다가 앞으로(오른쪽)으로 돌아오기
        move_l = i +  (len(name) - next_i) * 2
        
        move = min(move, move_r, move_l)
        
    return answer + move
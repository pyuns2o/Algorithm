import sys

input = sys.stdin.readline

n = int(input())
# N×N 형태의 보드임
board = [list(map(int, input().split())) for _ in range(n)]

# 회전 - 스티커랑 똑같음
def rotate(board):
    # NxN 형태니까 회전해도 어차피 똑같
    new = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[i][j] = board[n-1-j][i] # 회전 공식 외우기!
    
    return new

# 왼쪽으로 밀어서 합치는 함수 - 합쳐졌는지 표시하는 마크, 숫자 같으면 합치고 합쳐진거 표시, 제일 왼쪽.....
def merge_left(row):
    # 0을 지우고 왼쪽으로 쫙 모음
    nums = [x for x in row if x != 0]

    # 왼쪽부터 보면서 합치면 됨.
    merged = []
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i]==nums[i+1]:
            merged.append(nums[i]*2)
            i += 2 # 합쳐진 블록은 다시 합쳐지면 안되니까 뛰어 넘음.
        
        else:
            # 같은 숫자가 아니면 그냥 넣고 넘어가
            merged.append(nums[i])
            i += 1
    
    merged += [0] * (n - len(merged)) # 뒤에 빈 공간만큼 0으로 채우기
    return merged

# 상하좌우를 왼쪽으로 미는걸 그대로 두고 보드만 회전 시켜서 모두 적용하도록 하면 된다.

def tilt(board, dir):
    # dir만큼 회전 시키기
    for _ in range(dir):
        board = rotate(board)
    
    new_board = []
    # 모든 행에 대해서 왼쪽으로 밀어
    for i in range(n):
        new_board.append(merge_left(board[i]))

    # 회전시킨거 복구해 (4-dir)회전하면 복구됨
    for _ in range(4-dir):
        new_board = rotate(new_board) # 복구완
    
    return new_board

# 모든 경우에 대해서 완전 탐색을 진행하면 됨.
answer = 0

for tmp in range(4**5):
    c_board = [row[:] for row in board] # 카피뜨기

    brute = tmp
    for _ in range(5):
        dir = brute % 4 # 이동 방향
        brute //= 4
        c_board = tilt(c_board, dir)
    
    for i in range(n):
        for j in range(n):
            if c_board[i][j] > answer:
                answer = c_board[i][j]

print(answer)
def solution(triangle):
    for i in range(len(triangle) -2, -1, -1): # 맨 아래에서 한줄 위부터 돌기 시작
        for j in range(len(triangle[i])): # i줄에 있는 숫자 하나씩 확인
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]
        
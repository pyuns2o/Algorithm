from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)] # 최대 좌표 50 *2=100 -> +2 여유
    
    # 직사각형 2배 확장해서 채우기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        
        # 우선 전체를 1로 채워넣기
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] = 1
    # 내부 부분을 0으로 채우기를 따로 또 수행 1로 채우고 0으로 채우기를 한 반복문 안에서 하면 겹치는 부분에서 오류가 생길 수 있음..!!            
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        
        # 내부 영역을 0으로 넣어서 테두리만 1이도록 처리
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                board[x][y] = 0
                
    q = deque()
    visited = [[False] * 102 for _ in range(102)]
    
    sx, sy = characterX * 2, characterY * 2
    ex, ey = itemX * 2, itemY * 2
    
    q.append((sx, sy, 0))
    visited[sx][sy] = True
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while q:
        x, y, dist = q.popleft()
        
        if x == ex and y == ey:
            return dist // 2
        
        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]
            
            if 0<= nx < 102 and 0<= ny < 102:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
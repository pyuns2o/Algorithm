import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

note = [[0]*M for _ in range(N)] # 노트북
# paper는 스티커 도면

def rotate(paper):
    r, c = len(paper), len(paper[0])
    new = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            new[j][r-1-i] = paper[i][j]
    return new

def pastable(x,y,paper):
    r,c = len(paper), len(paper[0])

    for i in range(r):
        for j in range(c):
            if paper[i][j] == 1 and note[x+i][y+j] == 1: # 스티커 존재하는데 이미 붙어져 있다면
                return False
    
    for i in range(r):
        for j in range(c):
            if paper[i][j] == 1: # 스티커가 존재하는 칸이면
                note[x+i][y+j] = 1
    
    return True

for _ in range(K):
    r,c = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(r)]

    pasted = False

    for _ in range(4):
        r,c = len(paper), len(paper[0])

        for x in range(N-r+1):
            if pasted:
                break

            for y in range(M-c+1):
                if pastable(x,y,paper):
                    pasted = True
                    break
        if pasted:
            break

        paper = rotate(paper)

answer = sum(sum(row) for row in note)
print(answer)
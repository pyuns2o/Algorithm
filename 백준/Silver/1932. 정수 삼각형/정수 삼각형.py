n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2, -1, -1): # 아래에서 위로 올리면 됨 맨 아래줄 제외하고 쭉 올리면!!
    for j in range(len(tri[i])):
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])

print(tri[0][0]) # 제일 위에 올라온 값이 답이겠지!
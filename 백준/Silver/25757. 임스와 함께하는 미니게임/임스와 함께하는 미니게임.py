# 코드 간결화
import sys

n, game = sys.stdin.readline().split()
n = int(n)

# 처음부터 set으로 저장
user_set = {sys.stdin.readline().strip() for _ in range(n)}

# 집합 크기
uniq_count = len(user_set)

# 게임 종류에 따라 출력
if game == 'Y':
    print(uniq_count)
elif game == 'F':
    print(uniq_count // 2)
elif game == 'O':
    print(uniq_count // 3)
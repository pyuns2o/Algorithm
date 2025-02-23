import math

# 가로 세로 길이를
# 떨어져 앉아야 하는 값의 +1 한값으로 나눠서 올림을 하면 됨 (반올림 아님) 그걸 곱해줘
# h(세로) w(가로) n(세로칸) m(가로칸) 가 있다고 할때

h, w, n, m = map(int, input().split())

ga = math.ceil(h/(n+1))
se = math.ceil(w/(m+1))

opt = ga * se
print(opt)
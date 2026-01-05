m = input()
w = input()


cnt = 0
f = m.find(w)

while f != -1:
    cnt += 1
    f = m.find(w, f+len(w))

print(cnt)
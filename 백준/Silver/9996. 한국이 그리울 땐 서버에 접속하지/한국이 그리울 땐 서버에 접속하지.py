n = int(input())
pattern = input()

left, right = pattern.split('*')

for _ in range(n):
    name = input()

    if name.startswith(left) and name.endswith(right) and len(name) >= len(left) + len(right):
        print("DA")
    else:
        print("NE")

n = int(input())

for i in range(n):
    L, R = map(int, input().split())
    if L > R:
        L, R = R, L
    res = (R * (R + 1) // 2) - ((L - 1) * L // 2)
    print(res)

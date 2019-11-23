A, B, C = map(int, input().split())

b = B
ans = 0
while ans < C:
    b -= A
    if b < 0:
        break
    ans += 1
print(ans)

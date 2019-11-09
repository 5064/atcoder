N, K = map(int, input().split())

ans = 0

for i in range(1, N+1):
    score = i
    coeff = 0
    while score < K:
        score *= 2
        coeff += 1
    ans += (1/N)*((1/2)**coeff)

print(ans)

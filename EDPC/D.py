N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if w - WV[i][0] >= 0:  # 品物を追加できるとき
            dp[i+1][w] = max(dp[i+1][w], dp[i][w-WV[i][0]] + WV[i][1])
        # できないとき
        dp[i+1][w] = max(dp[i+1][w], dp[i][w])
print(dp[N][W])

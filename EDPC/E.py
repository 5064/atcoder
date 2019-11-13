N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]

V = 10**3
dp = [[float('INF')]*(N*(V+1)) for _ in range(N+1)]  # Nとv≦10**3の制約から取りうるvの範囲
dp[0][0] = 0

for i in range(N):
    for v in range((i+1)*(V+1)):  # N*(V+1) を (i+1)*(V+1)で計算量を減らす
        if v - WV[i][1] >= 0:  # 品物を追加できるとき
            dp[i+1][v] = min(dp[i+1][v], dp[i][v-WV[i][1]] + WV[i][0])
        # できないとき
        dp[i+1][v] = min(dp[i+1][v], dp[i][v])

ans = 0
for i in range(N*(V+1)):
    if dp[N][i] <= W:
        ans = i
print(ans)

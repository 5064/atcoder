# https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-6k%E5%80%8B%E4%BB%A5%E5%86%85%E9%83%A8%E5%88%86%E5%92%8C%E5%95%8F%E9%A1%8C
# 動的計画法で実装してみる

N, A = map(int, input().split())
x = list(map(int, input().split()))

max_of_a = N * A

# dp[i][j][k] := i枚目までからj枚取って、合計をkにする通り数
dp = [[[0] * (max_of_a + 1) for _ in range(N+1)]for _ in range(N+1)]
dp[0][0][0] = 1


for i in range(N+1):
    for j in range(N+1):
        for k in range(max_of_a + 1):
            if i >= 1 and x[i-1] > k:
                dp[i][j][k] = dp[i-1][j][k]
            elif i >= 1 and j >= 1 and x[i-1] <= k:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k - x[i-1]]

ans = 0
for j in range(1, N+1):
    # N枚(カード総数)の中から1枚以上取った時の、j枚取って合計がj*Aの所 の合計
    ans += dp[N][j][j*A]
print(ans)

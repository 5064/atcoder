N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
MOD = 10**9+7

is_safe = [True]*(N+1)
for a in A:
    is_safe[a] = False

dp = [0]*(N+1)
# 初期条件
dp[0] = 1
if is_safe[1]:
    dp[1] = 1

for i in range(2, N+1):
    if is_safe[i-1]:
        dp[i] += dp[i-1]
    if is_safe[i-2]:
        dp[i] += dp[i-2]
    dp[i] %= MOD

print(dp[N])

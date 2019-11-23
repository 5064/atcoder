N = int(input())
P = list(map(int, input().split()))

dp = [0]*(N*N+1)
for i in range(N):
    for j in range(N):
        dp[i] = dp[i] + dp[i-1]

print(dp)

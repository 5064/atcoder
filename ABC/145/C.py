from math import sqrt

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            pass
        elif i > j:
            dp[i][j] = dp[j][i]
        else:
            dp[i][j] = sqrt((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)

ans = 0
for i in range(N):
    for j in range(N):
        ans += dp[i][j]
print(ans/N)

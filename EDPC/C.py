N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] := i日目までにjを選んだときのmax幸福度
# j={A=0,B=1,C=2}の添え字を使うことにする
dp = [[0]*3 for _ in range(N+1)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:  # 前日と同じActivityは除外
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j]+ABC[i][k])

print(max(dp[N][0], dp[N][1], dp[N][2]))

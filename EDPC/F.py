S = input()
T = input()
len_s = len(S)
len_t = len(T)
# dp[i+1][j+1] := sのi文字目までとtのj文字目まででのLCSの長さ
dp = [[0]*(3001) for _ in range(3001)]

for i in range(len_s):
    for j in range(len_t):
        if S[i] == T[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])

# 遡って復元する
ans = ''
i = len_s
j = len_t
while i > 0 and j > 0:
    # (i-1, j) -> (i, j) と更新されていた場合
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    # (i, j-1) -> (i, j) と更新されていた場合
    elif dp[i][j] == dp[i][j-i]:
        j -= 1
    # (i-1, j-1) -> (i, j) と更新されていた場合
    else:
        ans = S[i-1] + ans  # s[i-1] == t[j-1] の場合であるので T[i-1] + ansでも同じ
        i -= 1
        j -= 1
print(ans)

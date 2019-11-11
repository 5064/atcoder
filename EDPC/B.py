N, K = map(int, input().split())
H = list(map(int, input().split()))

cost = [float('INF')]*N  # コスト比較のために、infinityで初期化
cost[0] = 0

for i in range(1, N):
    for k in range(1, K+1):
        if i-k < 0:  # indexが負の数にならないように
            break
        cost[i] = min(cost[i], cost[i-k]+abs(H[i-k]-H[i]))

print(cost[N-1])

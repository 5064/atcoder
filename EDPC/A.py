N = int(input())
H = list(map(int, input().split()))

cost = [0]*N
for i in range(1, N):
    if i == 1:
        cost[i] = cost[i-1]+abs(H[i-1]-H[i])
    else:
        cost[i] = min(cost[i-1]+abs(H[i-1]-H[i]), cost[i-2]+abs(H[i-2]-H[i]))
print(cost[N-1])

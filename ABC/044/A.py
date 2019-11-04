N = int(input())
K = int(input())
X = int(input())
Y = int(input())

cost = 0
for n in range(N):
    if n < K:
        cost += X
    else:
        cost += Y

print(cost)

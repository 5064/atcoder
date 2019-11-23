N = int(input())
W = list(map(int, input().split()))

ans = float('INF')
right = sum(W)
left = 0
for i, w in enumerate(W):
    left += w
    right -= w
    if abs(left-right) < ans:
        ans = abs(left-right)

print(ans)

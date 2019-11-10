N, M = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(M)]

min_id = 1
max_id = float('INF')
na_flag = False
for m in range(M):
    left = LR[m][0]
    right = LR[m][1]
    if right < min_id or max_id < left:
        na_flag = True
        break

    if min_id < left and left <= max_id:
        min_id = left
    if right < max_id and min_id <= right:
        max_id = right

if na_flag:
    print(0)
else:
    print(max_id - min_id + 1)

# TLE
# 部分点を獲得

from itertools import combinations, starmap

N, A = map(int, input().split())
x_list = list(map(int, input().split()))

coefficient = 1  # Aの係数
result = 0
while coefficient <= N:
    for r in range(1, N+1):
        multiple_of_a = coefficient * A
        combis_sums = map(sum, combinations(x_list, r))
        for combi_sum in combis_sums:
            if combi_sum == multiple_of_a:
                result += 1
        coefficient += 1

print(result)

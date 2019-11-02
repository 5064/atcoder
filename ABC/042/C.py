from sys import exit

N, K = map(int, input().split())
dislikes = list(map(int, input().split()))

LIMIT_N = 10000

while N < LIMIT_N:
    n_set = set(str(N))
    d_set = set([str(d) for d in dislikes])
    if n_set.isdisjoint(d_set):
        print(N)
        exit()
    N += 1

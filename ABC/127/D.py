# TLE


def solve(N, M, A, BC):
    for m in range(M):
        B, C = BC[m][0], BC[m][1]

        for _ in range(B):
            memo = -1
            start = 0
            if memo >= 0:
                start = memo
            for i in range(start, len(A)):
                if A[i] < C:
                    A[i] = C
                    memo = i
                    break
        A.sort()
    print(sum(A))


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]

    A.sort()
    solve(N, M, A, BC)

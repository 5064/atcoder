N = int(input())
TA = [list(map(int, input().split())) for i in range(N)]


t_votes = TA[0][0]
a_votes = TA[0][1]
for n in range(1, N):
    t_ratio = TA[n][0]
    a_ratio = TA[n][1]
    # coeff = 1
    # while TA[n][0] * coeff < t_votes or TA[n][1] * coeff < a_votes:
    #     coeff += 1
    # ↓
    coeff = max((t_ratio + t_votes - 1) // t_ratio,
                (a_ratio + a_votes - 1) // a_ratio)

    t_votes = coeff * t_ratio
    a_votes = coeff * a_ratio

print(t_votes + a_votes)

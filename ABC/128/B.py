N = int(input())
SP = [list(input().split()) for i in range(N)]

for i, sp in enumerate(SP):
    sp[1] = int(sp[1])
    sp.append(i+1)

SP.sort(key=lambda x: (x[0], -x[1]))
for sp in SP:
    print(sp[2])

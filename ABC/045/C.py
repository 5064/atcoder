# bit全探索

S = input().strip()

ans = 0
for i in range(2**(len(S)-1)):
    e = ['' if c == '0' else '+' for c in format(i, 'b').zfill(len(S))]
    ans += eval(''.join(a+b for a, b in zip(e, S)))
print(ans)

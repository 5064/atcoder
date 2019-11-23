S = input()

s = S
index = 0
ans = 0
while index < len(s)-1:
    c = s[index]
    next_c = s[index+1]
    if c != next_c:
        s = s[:index] + s[index+2:]
        index = 0
        ans += 2
    else:
        index += 1

print(ans)

S = input()

red = 0
blue = 0
for c in S:
    if c == '0':
        red += 1
    elif c == '1':
        blue += 1

print(min(red, blue)*2)

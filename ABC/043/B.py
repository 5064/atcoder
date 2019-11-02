s = input()

result = ''
for char in s:
    if char == 'B':
        result = result[:len(result)-1]
    else:
        result += char

print(result)

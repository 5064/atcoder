N, M = map(int, input().split())
strings = [input() for i in range(N)]

result = ''
for _ in range(N):
    index = strings.index(min(strings))
    result += strings[index]
    strings.pop(index)

print(result)

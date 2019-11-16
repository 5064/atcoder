N = int(input())
S = input()


if len(S) % 2 != 0:
    print('No')
    exit()

right = S[:len(S)//2]
left = S[(len(S)//2):]

ans = 'Yes'
for i, rc in enumerate(right):
    if left[i] != rc:
        ans = 'No'

print(ans)

N = int(input())
a = list(map(int, input().split()))


def mean(numbers):
    return sum(numbers) / len(numbers)


target = round(mean(a))
cost = 0
for num in a:
    cost += (num - target)**2

print(cost)

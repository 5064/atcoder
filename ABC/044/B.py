from collections import Counter

w = input()
values, counts = zip(*Counter(w).most_common())
for count in counts:
    if count % 2 == 0:
        continue
    else:
        print('No')
        exit()
print('Yes')

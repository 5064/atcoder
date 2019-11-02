from collections import Counter

s = input()
s_list = list(s)

NOT_FOUND = '-1 -1'
if len(s_list) == 1:
    print(NOT_FOUND)

most_common = Counter(s_list).most_common()[0]  # tuple
border_num = len(s) // 2  # 切り捨て

if most_common[1] > border_num:
    first_common_index = s.find(most_common[0])
    result = ''
    for i, char in enumerate(s[first_common_index:]):
        result += char
        if len(result) < 3:
            continue
        if Counter(result).most_common()[0][0] == most_common[0] and Counter(result).most_common()[0][1] > len(s) // 2:
            print(str(first_common_index) + ' ' + str(first_common_index + i))
            exit()
else:
    print(NOT_FOUND)

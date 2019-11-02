def equal_list(lst1, lst2):
    lst = lst1.copy()
    for element in lst2:
        try:
            lst.remove(element)
        except ValueError:
            break
    else:
        if not lst:
            return "YES"
    return "NO"


HAIKU = [5, 7, 5]
v = list(map(int, input().split()))
print(equal_list(v, HAIKU))

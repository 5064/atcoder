S = input()

left = int(S[:2])
right = int(S[2:])
left_mm_flag = False
left_yy_flag = False
right_mm_flag = False
right_yy_flag = False

if 0 <= left <= 99:
    left_yy_flag = True
    if 1 <= left <= 12:
        left_mm_flag = True


if 0 <= right <= 99:
    right_yy_flag = True
    if 1 <= right <= 12:
        right_mm_flag = True


if left_mm_flag and right_yy_flag and left_yy_flag and right_mm_flag:
    print('AMBIGUOUS')
elif left_yy_flag and right_mm_flag:
    print('YYMM')
elif left_mm_flag and right_yy_flag:
    print('MMYY')
else:
    print('NA')

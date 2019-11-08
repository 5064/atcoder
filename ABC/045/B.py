SA = input()
SB = input()
SC = input()

next_ = SA[0]
SA = SA[1:]
while True:
    if next_ == 'a':
        if len(SA) == 0:
            print('A')
            exit()
        next_ = SA[0]
        SA = SA[1:]
    elif next_ == 'b':
        if len(SB) == 0:
            print('B')
            exit()
        next_ = SB[0]
        SB = SB[1:]
    elif next_ == 'c':
        if len(SC) == 0:
            print('C')
            exit()
        next_ = SC[0]
        SC = SC[1:]

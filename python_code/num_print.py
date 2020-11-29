
for y in range(7):
    print(y + 1, ' ', end='')
    for x in range(8):
        if not (x == 7 and y == 6 or x == 6 and y == 6):
            p = y*8 + x
            print('|' + str(p).zfill(3), end='')
    print('|')
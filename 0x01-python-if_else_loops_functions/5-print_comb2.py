#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(str(i).format('02d'))
    else:
        print(format(i, '02d') + ", ", end="")

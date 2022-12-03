#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j:
            continue
        elif i != j and i < j:
            if i == 8 and j == 9:
                print(str(i) + str(j))
                break
            else:
                print((str(i) + str(j).format() + ", "), end="")

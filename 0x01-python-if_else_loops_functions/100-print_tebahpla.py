#!/usr/bin/python3
lower = list(range(122, 96, -1))
upper = list(range(90, 64, -1))
for i, j in zip(lower, upper):
    print(chr(i) + chr(j), end="")
print("")

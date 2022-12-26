d = {1: "one", 3: "three"}
d1 = {1: "two"}
num = 3
value = "six"
d2 = {num: value}
# updates the value of key 2
d.update(d2)
print(d)

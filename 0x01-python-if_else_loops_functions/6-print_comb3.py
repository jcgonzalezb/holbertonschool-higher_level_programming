#!/usr/bin/python3
for i in range(1, 89):
    if i in range(10, 12):
        continue
    if i in range(20, 23):
        continue
    if i in range(30, 34):
        continue
    if i in range(40, 45):
        continue
    if i in range(50, 56):
        continue
    if i in range(60, 67):
        continue
    if i in range(70, 78):
        continue
    if i in range(80, 89):
        continue
    print("{:02d}".format(i), end=', ')
print(89)

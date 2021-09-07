#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
ld = abs(number) % 10
if n < 0:
    ld = ld * -1
if ld > 5:
    print("Last digit of", n, "is", ld, "and is greater than 5")
elif ld == 0:
    print("Last digit of", n, "is", ld, "and is 0")
else:
    print("Last digit of", n, "is", ld, "and is less than 6 and not 0")

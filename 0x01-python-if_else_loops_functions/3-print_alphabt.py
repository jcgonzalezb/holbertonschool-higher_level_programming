#!/usr/bin/python3
for i in range(97, 123):
    if i in (ord('q'), ord('e')):
        continue
    print("{:c}".format(i), end='')

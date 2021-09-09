#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    j = 0
    if (n == 1):
        print("0")
    else:
        for i in range(1, n):
            j += int(sys.argv[i])

        print("{}".format(j))

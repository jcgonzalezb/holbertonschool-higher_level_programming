#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if (n == 1):
        print("0 arguments.")
    elif (n == 2):
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print("{}".format(n - 1), "arguments:")
        for i in range(1, n):
            print(i, ":", sys.argv[i])

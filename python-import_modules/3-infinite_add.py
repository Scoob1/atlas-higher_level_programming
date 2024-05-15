#!/usr/bin/python3
from sys import argv


def inf_add(argv):
    sum = 0
    for i in argv[1:]:
        sum += int(i)
    print(sum)


if __name__ == "__main__":
    inf_add(argv)

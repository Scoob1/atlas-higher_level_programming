#!/usr/bin/python3

for num in range(97, 123):
    if num == 101 or num == 113:
        pass
    else:
        print("{char}".format(char=chr(num)), end="")

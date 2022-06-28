#!/usr/bin/python3
def uppercase(string):
    new = ""
    for i in string:
        if 97 <= ord(i) < 123:
            new += chr(ord(i)-32)
        else:
            new += i
    print(new)

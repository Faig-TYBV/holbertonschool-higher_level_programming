#!/usr/bin/python3
def uppercase(str):
    for i in str:
        k = 0
        if ord(i) >= 97 and ord(i) <= 122:
            k = 32
        print("{}".format(chr(ord(i)-k)), end='')
    print("")

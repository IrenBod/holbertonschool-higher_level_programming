#!/usr/bin/python3

def uppercase(str):

    upp = ""
    for i in str:
        if 'a' <= i <= 'z':
            upp += chr(ord(i) - 32)
        else:
            upp += i
    print("{}".format(upp))

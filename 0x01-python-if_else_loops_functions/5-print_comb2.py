#!/usr/bin/python3

""" numbers with 2 digits from 0 through 99 """

for i in range (0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")

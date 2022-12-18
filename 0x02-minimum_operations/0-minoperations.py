#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def countProcess(num):
    """ Return list of process until n H """
     con = 2
    array = list()
    while (con <= x):
        if x % con == 0:
            array.append(con)
            x /= con
        else:
            con += 1
    return array



def minOperations(n):
    """ Return sum of process until n H """
     min = 0
    factors = [x for x in countProcess(n)]
    matter = {item: factors.count(item) for item in factors}
    for k, v in matter.items():
        min += k * v
    return min
#!/bin/env python3


import re


regex = r'^[hH][iI]\s[^Dd]'


def FindHi(test_string):
    res = re.search(regex, test_string) is not None
    # print('res {} for regex {} against test string {}'.format(
    #       res, regex, test_string))
    return res


if __name__ == '__main__':
    """
    Input: first line to have integer with number of following conversation lines.
    Output: print conversation line if it matches pattern.
    """
    n = int(input())
    for _ in range(n):
        s = str(input())
        if FindHi(s):
            print(s)

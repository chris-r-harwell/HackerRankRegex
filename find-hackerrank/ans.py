#!/bin/env python3


import re


def FindHackerRankScore(test_string):
    """
    -1 if line neither starts nore ends with hackerrank
     1 if line starts with hackerrank
     2 if line ends with hackerrank
     0 if line both starts and ends with hackerrank
    """
    score = -1  # assume none

    start = re.search(r'^hackerrank', test_string) is not None
    end = re.search(r'hackerrank$', test_string) is not None

    if start and end:
        score = 0
    elif end:
        score = 2
    elif start:
        score = 1

    return score


if __name__ == '__main__':
    """
    first line to have integer with number of following conversation lines
    """
    n = int(input())
    for _ in range(n):
        s = str(input())
        m = FindHackerRankScore(s)
        print(m)

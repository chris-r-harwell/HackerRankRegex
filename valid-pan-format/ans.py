#!/bin/env python3
# \w word char [0-9 a-Z]
# \W non-word
# \s whitespace
# \S non-whitspace
# [^a] not a
# \d digit [0-9]
# \D not digit
# ^ start of line
# $ end of line
# [a-z] all lower alpha char from a to z inclusive
# [A-Z] all upper alpha char from A to Z inclusive
# [0-9] all digits from 0 to 9 inclusive
#
# {n} matches preceding item exactly n times
# {n,m} matches preceding item at least n and no more than m times inclusive
# * matches preceding item 0 or more times
# + matches preceding item 1 or more times

import re


regex_pattern = r'^[A-Z]{5}\d{4}[A-Z]{1}$'


def ValidUtopianID(test_string):
    valid = re.search(regex_pattern, test_string) is not None
    return valid


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = str(input())
        if ValidUtopianID(s):
            print("YES")
        else:
            print("NO")

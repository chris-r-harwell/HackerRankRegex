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


regex_pattern = r'^[a-zA-Z]*s$'

test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

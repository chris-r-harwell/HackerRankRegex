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
# {n,} matches preceding item at least n times

import re


regex_pattern = r'^\d{1,2}[a-zA-Z]{3,}[\.]{0,3}$'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

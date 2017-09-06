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
#

import re


regex_pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

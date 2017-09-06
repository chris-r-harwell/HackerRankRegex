#!/bin/env python3
#
# ^ start of line
# $ end of line
# \. literal .
# \w word char

import re


regex_pattern = r'^\d(\w){4}\.$'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

#!/bin/env python3

import re


regex_pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

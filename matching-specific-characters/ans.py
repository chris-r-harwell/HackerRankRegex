#!/bin/env python3
# \w word char [0-9 a-Z]
# \W non-word

import re


regex_pattern = r'^[123][120][xs0][30Aa][xsu][\.,]$'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

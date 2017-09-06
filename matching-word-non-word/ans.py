#!/bin/env python3
# \w word char [0-9 a-Z]
# \W non-word

import re


regex_pattern = r'(\w){3}\W(\w){10}\W(\w){3}'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

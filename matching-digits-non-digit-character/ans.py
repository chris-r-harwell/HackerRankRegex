#!/bin/env python3
# \d digit [0-9]
# \D non-digit

import re


regex_pattern = r'\d\d\D\d\d\D\d\d\d\d'
regex_pattern = r'(\d\d\D){2}(\d){4}'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

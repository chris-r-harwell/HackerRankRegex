#!/bin/env python3
# \S non-whitespace
# \s whitespace [ \r\n\t\f ]

import re


# regex_pattern = r'\S\S\s\S\S\s\S\S'
regex_pattern = r'(\S\S\s){2}(\S){2}'
test_string = input()

search = re.search(regex_pattern, test_string) is not None

print(str(search).lower())

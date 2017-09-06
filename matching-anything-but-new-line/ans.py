#!/bin/env python3
# [^\n] anything but a newline

import re
import sys


regex_pattern = r'^...\....\....\....$'
regex_pattern = r'^[^\n]{3}\.[^\n]{3}\.[^\n]{3}\.[^\n]{3}$'
test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())

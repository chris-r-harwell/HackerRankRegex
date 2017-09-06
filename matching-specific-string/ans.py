#!/bin/env python3

import re


Regex_Pattern = r'hackerrank'
Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

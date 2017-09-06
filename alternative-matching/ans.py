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
# \b position at word boundary, 3 cases:
#  1. before 1st word char in string
#  2. between two char in the string
#      where one is a word char and the other is not
#  3. after last word char in a string
#
# {n} matches preceding item exactly n times
# {n,m} matches preceding item at least n
#        and no more than m times inclusive
# * matches preceding item 0 or more times
# + matches preceding item 1 or more times
# () can be used to create a capturing group for back reference
# (?:) can be used to create a non-capturing group.
#    . useful if we do not need the group to capture its match
# (ABC|def) where | is an alternation and will match either
#   ABC or def
#   . inside groups matches up to ( or ) or |
#
# [A|D]  where | is an alternation and will match either
#   A or D
#   . inside character classes matches only single letters


import re


Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'
test_string = input()

search = re.search(Regex_Pattern, test_string) is not None

print(str(search).lower())

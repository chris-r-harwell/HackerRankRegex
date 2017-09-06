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
#
# \group_number, use to refer to a match in ()
#  \0 refers to entire match
#  \1 to first grouping inside ()
#

# capturing group that match nothing:
# (b?) where ? means optional and matches nothing (b is literal(
#   . \1 will refer to this even if it optionally matched nothing
#
# capturing group that didn't participate in match at all
# (b)? where ? means optional group and fails to match nothing
#   . \1 will not refer to this if there was no match.
#
# ? inside () will match nothing, so \1 works
# ? outside () will not match nothing, so \1 fails
#
# assertions:
#  assertion, positive lookahead:
#   regex_1(?=regex_2) matches regex_1 if regex_2 found, but
#   regex_2, the lookahead, is excluded from match. It does
#   not return matches of regex_2. Only asserts wheter a match
#   is possible or not.
#
#  assertion, negative lookahead:
#   regex_1(!?regex_2) matches regex_1 if regex_2 not found
#
#  assertion, positive lookbehind:
#   (?<=regex_2)regex_1 asserts regex_1 to be immediately
#   preceeded by regex_2. Lookbehind is excluded from match
#   do not consume matches of regex_2, but only asserts whether
#   a match is possible or not.
#
#  assertion, negative lookbehind:
#   (?<!regex_2)regex_1 asserts regex_1 is not immediately
#   preceeded by regex_2.


import re


Regex_Pattern = r'(?<![aeiouAEIOU]).'
test_string = input()

match = re.findall(Regex_Pattern, test_string)

print("Number of matches :", len(match))

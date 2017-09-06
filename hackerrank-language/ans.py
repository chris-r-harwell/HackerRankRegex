#!/bin/env python3


import re


regex = r'^\d{1,5}\s+(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'


def FindHi(test_string):
    res = re.search(regex, test_string) is not None
    # print('res {} for regex {} against test string {}'.format(
    #       res, regex, test_string))
    return res


if __name__ == '__main__':
    """
    Input: first line to have integer
        with number of following api request lines.
    Output: print api request line if it matches pattern.
    """
    n = int(input())
    for _ in range(n):
        s = str(input())
        if FindHi(s):
            print('VALID')
        else:
            print('INVALID')

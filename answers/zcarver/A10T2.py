#! /usr/bin/env python
# encoding UTF-8

'''
Assignment10Task2 biol7800
ZacCarver 03/01/2016
Take the given Stars text from T1 and do the same using the 'Counter'dictionary
'''

import re
from collections import Coutner


def cntdw(f):
    # finds all alphanumeric chars, reads the file in a str and lowers the case
    swrds = re.findall('\w+', f.read().lower())
    # counts the itemized words from file and keeps the most frequent
    cntdw = Counter(swrds).most_common(10)
    print(cntdw)


def main():
    f = open('Stars.txt', 'r')
    cntdw(f)

if __name__ == '__main__':
    main()

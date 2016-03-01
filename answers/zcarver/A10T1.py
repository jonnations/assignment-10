#! /usr/bin/env python
# encoding UTF-8

'''
Assignment10Task1 biol7800
ZacCarver 03/01/2016
Take the given Stars text and process using a 'standard' dictionary
'''

import re
import operator
from collections import defaultdict


def sw(f):
    # finds all alphanumeric chars, reads the file in a str and lowers the case
    swrds = re.findall('\w+', f.read().lower())
    # designates a dictionary
    wrddict = {}
    for word in swrds:
        if word in wrddict:
            # for each occurance of an itemized word counts up by 1.
            wrddict[word] += 1
        else:
            wrddict[word] = 1
    # fetches items of dictionary as tuple and reverses order.
    # http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    sw = sorted(wrddict.items(), key=operator.itemgetter(1), reverse=True)
    # prints only the 'top' ten.
    print(sw[:10])


def main():
    f = open('Stars.txt', 'r')
    sw(f)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 10
Task 2 Program: Using the `counter` dictionary subclass to count words
Jessie Salter
26 February 2016
"""

from collections import Counter

from jsalt10_task1 import formatter
# Imports the text and formats it for accurate word count
from jsalt10_task1 import top_ten
# Sorts the pairs of words:counts, prints top ten in order


def wc_dict(doc):
    '''Uses the Counter subclass from the collections module to create a
    dictionary where each word in the doc is a key and the value is the
    number of times it appears in the text.'''
    wc = Counter(doc)
    return wc


def main():
    '''Calls functions I previously wrote to import the text, format it, and
    then print the desired results.'''
    doc = formatter('stars.txt')
    results = wc_dict(doc)
    top_ten(results)

if __name__ == '__main__':
    main()

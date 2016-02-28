#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 10
Task 1 Program: Using Dictionaries for Word Counts
Jessie Salter
25 February 2016
"""

import re


def formatter(my_file):
    '''Imports the contents of the file and converts them to a string.
    Uses regular expressions to remove punctuation & whitespace.
    Then lowercases each word from the file'''
    with open(my_file) as doc:
        doc_string = doc.read()
        # Imports text as a string
        doc_list = re.split('\W+', doc_string)
        # Splits string into individual words; strips whitespace/punctuation
        formatted_list = [str.lower(word) for word in doc_list]
        # Lowercases all words
    return formatted_list


def counter(doc):
    '''Counts the occurrence of each word in the list by creating
    a dictionary where the value of each word (key) is the word count.'''
    word_count = dict()
    for word in doc:
        count = word_count.get(word, 0)
        # Makes each word in the list a key and assigns it a value of 0
        word_count[word] = 1 + count
        # Every time a word appears in the document, its value increases by 1
    return word_count


def top_ten(wc_dict):
    '''Creates list with each word:count pair as a list item, allowing it to
    be sorted from highest to lowest occurrence. Prints the top ten words in
    order from most used to least.'''
    wc_list = []
    for word, count in wc_dict.items():
        wc_list.append([count, word])
        # Creates a list with each count/word as its own list. Putting the
        # count first allows this list to be sorted in the next command
    final_list = sorted(wc_list, reverse=True)
    # Sorts the list from highest to lowest (i.e. most common word first)
    for x in range(0, 10):
        # Accesses first ten wordcount pairs in the list using iteration
        print(
            repr(final_list[x][1]).rjust(9),
            # repr() keeps quotes around the word (1st element of each list)
            str('occurs').rjust(6),
            str(final_list[x][0]).rjust(2),
            # the 0th element of the list is the word count
            str('times').rjust(5))
        # .rjust(x) right-justifies the output where the column is x char long


def main():
    formatted = formatter('stars.txt')
    word_count = counter(formatted)
    top_ten(word_count)

if __name__ == '__main__':
    main()

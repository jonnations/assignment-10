#!/usr/bin/env python

"""
Task 2:
Using Counter from the collections module, write a program to count word usage
in the same text as above. Have this program print out, in decreasing order
(most common to least common) the 10 most common words and the count of each
word used. As always, your program should contain a main loop and an ifmain
statement, and it should be formatted correctly.

Created by Shraddha Shrestha on February 29, 2016
Copyright 2016. All rights reserved.

"""

from collections import Counter


def frequent_word(text):
    word_edit_1 = text.upper().replace("\n", " ").replace("'", "").replace(","
    , "").replace(".", "")
    word_edit_2 = word_edit_1.split()
    common_words = Counter(word_edit_2).most_common(10)
    return common_words


def main():
    text = """Stars burn a very light type of air that is packed very tight in
    the middle of the star. The tiny pieces of the air join to form a slightly
    heavier type of air that can't burn in the star without the middle being
    much hotter and tighter. After a long time, all the very light air in the
    middle is used up. Then the star gets much hotter and tighter in the
    middle, so it can burn the slightly heavier air. It also also gets much
    bigger and cooler outside. But it is still so hot it will burn up any
    close-in worlds. The sun is a star and will do this after a very long time.
    It will get so big that it will burn our world all up. This will not happen
    for at least ten hundred hundred hundred hundred years, so we don't have to
    worry about it now. Long after that, a star like the sun will burn up all
    the slightly heavier air, too. Then it will become very tiny and hot and
    white, but will be so tiny it won't be able to keep its worlds warm.
    It will keep cooling off over a very very long time. The worlds that are
    left will be all ice. But stars that are heavier can go on to burn heavier
    and heavier things, until finally they make the biggest flash we know.
    That is their end."""

    result = frequent_word(text)
    print("The 10 common words are:\n ", result)
    

if __name__ == '__main__':
	main()

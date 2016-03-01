#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 10

Task 2

This program uses Counter and most_common to generate a list of the top ten most used words in the string
(after the string has been reformatted).

Elisa Elizondo
"""

from collections import Counter

string = "Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air \n\
join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.\n\
After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle,\n\
 so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will \n\
burn up any close-in worlds. The sun is a star and will do this after a very long time. It will get so big that it will\n\
 burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have\n\
 to worry about it now.Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it\n\
 will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep\n\
 cooling off over a very very long time. The worlds that are left will be all ice. But stars that are heavier can go\n\
 on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end."

def format_string(string):
   string = string.lower()
   string = string.replace("\n", " ")
   string = string.replace(".", " ")
   string = string.replace("  ", " ").replace("   ", " ")
   string2= string.split(' ')
   return string2


def word_count(string2):
    top = Counter(string2).most_common(10)
    return top

def main():
    string2 = format_string(string)
    top_ten = word_count(string2)
    print(top_ten)


if __name__ == '__main__':
    main()

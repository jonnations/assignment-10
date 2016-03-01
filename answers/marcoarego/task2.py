# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 19:55:33 2016

@author: Marco
"""

"""
Task 2
There are several special types of dictionaries, including ordereddict, 
defaultdict, and Counter. In fact, Counter is built expressly for tasks similar
to the one that I've laid out, above.

Using Counter from the collections module, write a program to count word 
usage in the same text as above. Have this program print out, in decreasing 
order (most common to least common) the 10 most common words and the count of 
each word used. As always, your program should contain a main loop and an 
ifmain statement, and it should be formatted correctly.

"""

# importing modules
import collections
import re

# Global Variables
STRING = ('''Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end.''')


def string_standizer(string):
    '''
    this function takes all kinds of pontuation out of our string, including
    the apostrophe (') of words like can't, for example. The output will
    comprehend a lower case string with words separated by spaces.
    '''
    low = string.lower()
    without_pontuation = re.sub("\W"," ",low)
    one_space = re.sub("\s+"," ",without_pontuation)
    end_stripper = one_space.strip()
    return end_stripper


def counter_function(string):
    '''
    The input is a string. 
    this function uses the Counter function from the collections' module to
    count the values in a list and return a dictionary with the number of
    occurrencies for each word
    '''
    string_list = string_standizer(string)
    listagem = string_list.split(" ")
    count = collections.Counter(listagem)
    return count


def main(string, n):
    words = counter_function(string)
    more_freq = words.most_common(n)
    for word,freq in more_freq:
        print(word+': '+str(freq))
    return more_freq
    

if __name__ == '__main__':
    main(STRING, 10)        
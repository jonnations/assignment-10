#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
22 Feb 2016
Assignment 10 Task 2

A program to count word usage. Prints out, in decreasing order (most common to
least common) the 10 most common words and the count of each word used.
'''

import string
from collections import Counter

stars = '''
Stars burn a very light type of air that is packed very tight in the middle
of the star. The tiny pieces of the air join to form a slightly heavier type
of air that can't burn in the star without the middle being much hotter and
tighter.

After a long time, all the very light air in the middle is used up. Then the
star gets much hotter and tighter in the middle, so it can burn the slightly
 heavier air. It also also gets much bigger and cooler outside. But it is still
 so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so big
that it will burn our world all up. This will not happen for at least ten
hundred hundred hundred hundred years, so we don't have to worry about it now.

Long after that, a star like the sun will burn up all the slightly heavier air,
too. Then it will become very tiny and hot and white, but will be so tiny it
won't be able to keep its worlds warm. It will keep cooling off over a very
very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things, until
finally they make the biggest flash we know. That is their end.
'''

exclude = set(string.punctuation)


def remove_punct(text=stars):
    remove_ch = ''.join(ch for ch in text if ch not in exclude)
    lower_case = remove_ch.lower()
    replace_data = lower_case.replace('\n', '')
    split_data = replace_data.split(' ')
    return(split_data)


def histogram2():
    count = Counter(remove_punct())
    for val, freq in count.most_common(10):
        print(val, freq)


def main():
    print("The 10 most used words are: ")
    remove_punct()
    histogram2()

if __name__ == '__main__':
    main()

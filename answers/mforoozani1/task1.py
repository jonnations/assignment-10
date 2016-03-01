#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to Write a program to count word usage in the text
count the most 10 common words
"""


string = """Stars burn a very light type of air that is packed very tight in the
         middle of the star. The tiny pieces of the air join to form a slightly
         heavier type of air that can't burn in the star without the middle
         being much hotter and tighter.
         After a long time, all the very light air in the middle is used up.
         Then the star gets much hotter and tighter in the middle, so it can
         burn the slightly heavier air.
         It also also gets much bigger and cooler outside. But it is still
         so hot it will burn up any close-in worlds.The sun is a star and will
         do this after a very long time. It will get so big that it will burn
         our world all up. This will not happen for at least ten hundred
         hundred hundred hundred years, so we don't have to worry about it now.
         Long after that, a star like the sun will burn up all the slightly
         heavier air, too. Then it will become very tiny and hot and white, but
         will be so tiny it won't be able to keep its worlds warm. It will keep
         cooling off over a very very long time. The worlds that are left will
         be all ice.
         But stars that are heavier can go on to burn heavier and heavier
         things, until finally they make the biggest flash we know. That is
         their end. """


def lowercase_replace(string):
    """
    remove, and change all characters to lower case
    """
    text_1 = string.replace(",", " ").replace(".", " ").casefold()
    text_2 = text_1.split()
    return text_2


def wordListToFreqDict(textlist):
    """
    count the frequency of the words and make dictionary
    """
    wordfreq = [textlist.count(p) for p in textlist]
    return dict(zip(textlist, wordfreq))


def sort_freqdict(freqdict):
    """
    sort them from high to low frequency, return top 10
    """
    A = [(freqdict[key], key) for key in freqdict]
    A.sort()
    A.reverse()
    return A


def main():
    result1 = lowercase_replace(string)
    result2 = wordListToFreqDict(result1)
    result3 = sort_freqdict(result2)
    for i in result3[0:10]:
        print(i[1], i[0])

if __name__ == '__main__':
    main()

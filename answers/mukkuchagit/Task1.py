#!/usr/bin/env python
# encoding: utf-8
"""
Dict and Tuples; assignment 10.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import operator

text = '''Stars burn a very light type of air that is packed very
tight in the middle of the star. The tiny pieces of the air join to form a
slightly heavier type of air that can't burn in the star without the
middle being much hotter and tighter.

After a long time, all the very light air in the middle is used up.
Then the star gets much hotter and tighter in the middle, so it can
burn the slightly heavier air. It also also gets much bigger and
cooler outside. But it is still so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so
big that it will burn our world all up. This will not happen for at least
ten hundred hundred hundred hundred years, so we don't have to worry about
it now.

Long after that, a star like the sun will burn up all the slightly heavier
air, too. Then it will become very tiny and hot and white, but will be so
tiny it won't be able to keep its worlds warm. It will keep cooling off
over a very very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things,
until finally they make the biggest flash we know. That is their end.'''


def blunt_word(text):
        lower_text = text.lower()
        wordstring = lower_text.replace(".", "").replace(",", "").replace("\n\n", "").replace("\n", "")
        return wordstring


def word_list(wordstring):
    wordlist = wordstring.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(str(wordlist).count(w))
    return dict(zip(wordlist, wordfreq))


def sort_top_ten(Zip_list):
    T10 = sorted(Zip_list.items(), key=operator.itemgetter(1), reverse=True)[:10]
    return T10


def main():
    wordstring = blunt_word(text)
    Zip_list = word_list(wordstring)
    Top_10_words = sort_top_ten(Zip_list)
    print("Here is the list of the top 10 words:\n" + str(Top_10_words) + "\n")


if __name__ == '__main__':
    main()

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 10
Oscar Johnson 28 February 2016
"""

import re
import collections


def quote_dict(text):
    """
    function takes text as a string and creates a dictionary of words
    then returns a count of the 10 most common words as a list of tuples, 
    sorted by decreasing abundance
    Also returns count of all words as a list of tuples
    """
    text = text.lower()
    text = re.sub("['-,\n]", '', text) #remove non-alphanumeric chars and \n
    text = re.sub('[.]', ' ', text) #replace periods with whitespace
    #text = re.sub('  ', ' ', text)
    l = text.split() #listify
    # extract count of 10 most common words
    most_common = collections.Counter(l).most_common(10)
    # count of all words
    count_all = collections.Counter(l)
    return(most_common, count_all)



def main():
    my_quote = """Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end.
    """
    count = quote_dict(my_quote)
    print('ten most common words and count')
    for word in count[0]:
        print(word[0], word[1])
    
if __name__ == '__main__':
    main()
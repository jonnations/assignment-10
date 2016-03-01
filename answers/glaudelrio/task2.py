#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 20:13:05 2016

@author: Glaucia
"""
"""
Task 2
There are several special types of dictionaries, including ordereddict, defaultdict, and Counter. 
In fact, Counter is built expressly for tasks similar to the one that I've laid out, above.

Using Counter from the collections module, write a program to count word usage in the same
text as above. Have this program print out, in decreasing order (most common to least common) 
the 10 most common words and the count of each word used. As always, your program should 
contain a main loop and an ifmain statement, and it should be formatted correctly.
"""

import collections 

def counting_wordscounter(wordstring):
    """prints out the 10 most common words in a text with its frequency in a decrescent order (using Counter)"""
    #transforming all the words in lower case    
    wordstring=wordstring.lower()
    for word in wordstring:
        #removing commas
        wordstring=wordstring.replace(",","")
        #removing periods
        wordstring=wordstring.replace(".","")
        #removing new lines
        wordstring=wordstring.replace("\n","")
    #creating a list from the string
    wordlist = wordstring.split()
    #using counter to create a dictionary with words frequencies
    counterdict=collections.Counter(wordlist)
    #getting only the 10 most frequent words from this dictionary
    top10=counterdict.most_common(10)
    #passing the values into a list of lists to print them sorted
    listoflists=(sorted(top10, key=lambda top10: top10[1],reverse=True))
    #iterating across lists to print words and respective frequencies
    for lis in listoflists:
        #printing words with their frequencies
        print(lis[0],":",lis[1])


def main():
    Stars="""Stars burn a very light type of air that is packed very tight in the middle of the star. 
    The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the 
    star without the middle being much hotter and tighter.

    After a long time, all the very light air in the middle is used up. Then the star gets 
    much hotter and tighter in the middle, so it can burn the slightly heavier air. It also 
    also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

    The sun is a star and will do this after a very long time. It will get so big that it will burn our
    world all up. This will not happen for at least ten hundred hundred hundred hundred years, 
    so we don't have to worry about it now.

    Long after that, a star like the sun will burn up all the slightly heavier air, too. 
    Then it will become very tiny and hot and white, but will be so tiny it won't be able 
    to keep its worlds warm. It will keep cooling off over a very very long time. The worlds 
    that are left will be all ice.

    But stars that are heavier can go on to burn heavier and heavier things, until finally they make 
    the biggest flash we know. That is their end. """
    counting_wordscounter(Stars)

    
if __name__ == '__main__':
    main()   
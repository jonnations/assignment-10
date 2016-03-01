#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 18:44:31 2016

@author: Glaucia
"""
"""
Task 1
Here is a text description of How Stars Age, written using the ten hundred most common words 
(e.g. the Up-Goer Five Challenge).

Stars burn a very light type of air that is packed very tight in the middle of the star. 
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
the biggest flash we know. That is their end.



Write a program to count word usage in the text above. Have this program print out, 
in decreasing order (most common to least common) the 10 most common words and the count of 
each word used. As always, your program should contain a main loop and an ifmain statement, 
and it should be formatted correctly. You should use a standard dictionary as part of your function(s) t
o accomplish this task (see Task 2, where you'll use a slightly different type of dictionary).

"""

import operator

def counting_words(wordstring):
    """prints the ten most common words in a text with its count"""
    #transforming all the words in lower case    
    wordstring=wordstring.lower()
    for word in wordstring:
        #removing commas
        wordstring=wordstring.replace(",","")
        #removing periods
        wordstring=wordstring.replace(".","")
        #removing new lines
        wordstring=wordstring.replace("\n","")
    #splitting the string in a list
    wordlist = wordstring.split()
    #creating empty list to store words freq
    wordfreq = []
    #creating empty list to store most common words    
    words=[]
    #iterating across list values
    for w in wordlist:
        #storing words count in a list
        wordfreq.append(wordlist.count(w))
        #storing most common words in other list
        words.append(w)
    #zipping these two lists in a dictionary
    mydictionary=dict(zip(words,wordfreq))
    #sorting the dictionary to have only the 10 most common words
    sorteddict=dict(sorted(mydictionary.items(), key=operator.itemgetter(1), reverse=True)[:10])
    #oppen list to store keys and values of a dictionary
    dictlist=[]  
    #iterating across dictionary keys and values
    for key, value in sorteddict.items():
        newlist = [value,key]
        #appending keys and values in lists inside a list
        dictlist.append(newlist)
    #sorting the list from most common to less common
    listoflists=(sorted(dictlist, reverse=True))
    #iterating across list of values to print most common words sorted
    for lis in listoflists:
        print(lis[1],":",lis[0])

 
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
    counting_words(Stars)

    
if __name__ == '__main__':
    main()       

#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 10

Task 1

This program produces the top ten most frequently used words in the paragraph provided by reformatting
the string, splitting the string into individual words, storing the words in a dictionary, sorting said
dictionary, and printing the top ten words.

Elisa Elizondo
"""
import string

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

def make_list(string):
   string = string.lower()
   string = string.replace("\n", " ")
   string = string.replace(".", " ")
   string = string.replace("  ", " ").replace("   ", " ")
   string2= string.split(' ')
   return string2

def make_dict(string2):
    dict1 = {}
    for item in string2:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    return dict1

def top(dict2):
    dict3 = sorted(dict2.items(), key=lambda item: -item[1])
    return dict3[0:10]

def main():
    string2 = make_list(string)
    dict2 = make_dict(string2)
    dict4 = top(dict2)
    print("The top ten words are:", dict4)


if __name__ == '__main__':
    main()

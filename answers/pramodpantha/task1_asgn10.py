#!/usr/bin/env python
# utf-8

"""
Assignment 10,task1
Created by Pramod Pantha on March 1, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""
import operator


def paragraph(albert):
    """
    it removes given characters, and change all the characters to lower case
    """
    new_albert = albert.lower().replace('  ', ' ').replace(',', '') .replace(".
                ", "").casefold().split(" ")
    my_dict = {}
    for items in new_albert:
        my_dict[item] = new_albert.count(item)
    return my_dict


def ordered(string_dict):
    # it will first sort my_dict by occurance and prints the top 10 words
    print(sorted(albert_dict.items(), key=operator.itemgetter(1), reverse=True)
    [:10])


def main():
    albert = """Stars burn a very light type of air that is packed very tight in
    the middle of the star. The tiny pieces of the air join to form a slightly
    heavier type of air that can't burn in the star without the middle being
    much hotter and tighter. After a long time, all the very light air in the
    middle is used up. Then the star gets much hotter and tighter in the middle
    ,so it can burn the slightly heavier air. It also also gets much bigger and
    cooler outside. But it is still so hot it will burn up any close-in worlds.
    The sun is a star and will do this after a very long time. It will get so
    big that it will burn our world all up. This will not happen for at least
    ten hundred hundred hundred hundred years, so we don't have to worry about
    it now. Long after that, a star like the sun will burn up all the slightly
    heavier air, too. Then it will become very tiny and hot and white, but will
    be so tiny it won't be able to keep its worlds warm. It will keep cooling
    off over a very very long time. The worlds that are left will be all ice.
    But stars that are heavier can go on to burn heavier and heavier things,
    until finally they make the biggest flash we know. That is their end."""
    albert_dict = paragraph(albert)
    ordered(albert_dict)


if __name__ == '__main__':
    main()

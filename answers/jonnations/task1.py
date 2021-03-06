#!/usr/bin/env python
# utf-8

"""
Assignment 10, Task 1
Jon Nations on 25 February 2016

"""

import operator


def paragraph(stars):
    # removes punctuation, capitals, and turns the string into a
    # word-by-word dictionary
    new_stars = stars.replace('.', ' ').replace(',', ' ').replace('  ', ' ').lower().split(' ')
    my_dict = {}
    for item in new_stars:
        my_dict[item] = new_stars.count(item)
    return my_dict


def ordered(star_dict):
    # sorts the dictionary by occurances, then prints
    # the top 10 most-used words
    print(sorted(star_dict.items(), key=operator.itemgetter(1), reverse=True)[:10])


def main():
    stars = "Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds. The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now. Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice. But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end."
    star_dict = paragraph(stars)
    ordered(star_dict)


if __name__ == '__main__':
    main()

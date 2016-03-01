#!/usr/bin/env python
# encoding: utf-8

"""
This program examines a long string and find and counts each unique word. It
then places each word and its corresponding count value into a standard
dictionary where they are sorted and the top 10 most common words are printed
in decreasing order.

Edited by Alicia Reigel. 26 February 2016.
Copyright Alicia Reigel. Louisiana State University. 26 February 2016. All
rights reserved.

"""


def fixing_the_string(a_string):
    """funtion removes punctation, capitalization, makes each word a string"""
    the_list = a_string.replace('.', '').replace(',', '').lower()
    the_new_list = the_list.replace('\n', '').replace("'", '').split()
    return the_new_list


def puttin_it_in_a_dict(a_list):
    """creates a dictionary with each unique word as a key entry; counts the
    occurrence of each word to create the value for each key"""
    my_dict = {}
    for x in a_list:
        if x not in my_dict:
            my_dict[x] = 1
        else:
            my_dict[x] += 1
    return my_dict


def sort_that_dict(a_dict):
    """turns the dictionary key:value into a list of items and sorts it"""
    silly_list = []
    for key, value in a_dict.items():
        silly_list.append([value, key])
    silly_final_list = sorted(silly_list, reverse=True)
    return silly_final_list


def main():
    long_string = '''Stars burn a very light type of air that is packed very
    tight in the middle of the star. The tiny pieces of the air join to form a
    slightly heavier type of air that can't burn in the star without the middle
    being much hotter and tighter. After a long time, all the very light air in
    the middle is used up. Then the star gets much hotter and tighter in the
    middle, so it can burn the slightly heavier air. It also gets much bigger
    and cooler outside. But it is still so hot it will burn up any close-in
    worlds. The sun is a star and will do this after a very long time. It will
    get so big that it will burn our world all up. This will not happen for at
    least ten hundred hundred hundred hundred years, so we don't have to worry
    about it now. Long after that, a star like the sun will burn up all the
    slightly heavier air, too. Then it will become very tiny and hot and white,
    but will be so tiny it won't be able to keep its worlds warm. It will keep
    cooling off over a very very long time. The worlds that are left will be
    all ice. But stars that are heavier can go on to burn heavier and heavier
    things, until finally they make the biggest flash we know. That is their
    end.'''
    the_list = fixing_the_string(long_string)
    my_dict = puttin_it_in_a_dict(the_list)
    final_list = sort_that_dict(my_dict)
    for pair in final_list[:10]:
        print(pair[1], pair[0])


if __name__ == '__main__':
    main()

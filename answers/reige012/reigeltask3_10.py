#!/usr/bin/env python
# encoding: utf-8

"""
This program take run data and orders it into a list with the likelihood value
and then determines the best run based on the likelihood (e.g. value closest
to zero).

**Note to reviewer: You will need also download the data.txt file along with
this .py program. Make sure they are both in th same folder before running the
script. This can be tricky on Windows, but has been checked on two other
computers (besides mine) and appears to be working properly if these directions
are follwed. Thanks!**

I would like to sincerely thank the few individuals in class who have helped
me to overcome my brain blocks on this assignment by strategically leading me
to the correct methods without giving me the answers: Jessie S., Amie S. :)

Edited by Alicia Reigel. 28 February 2016.
Copyright Alicia Reigel. Louisiana State University. 28 February 2016. All
rights reserved.

"""


import os


def make_a_list(a):
    """opens the file and splits it into a list"""
    with open(a) as data:
        lines = data.read().splitlines()
        # splits each line into a list entry
    counter = 0
    for x in lines:
        lines[counter] = x.split('\\t')
        # splits each item separated by a tab into a new list entry
        counter += 1
    return lines


def list_to_dict(a_list):
    thee_dictionary = {}
    for x in a_list:
        # puts each nested list index=0 as a new key in the dictionary and
        # sets it equal to the same list entry index=2
        if x[0] not in thee_dictionary:
            thee_dictionary[x[0]] = x[2]
    return thee_dictionary


def print_it_pretty(dictionary):
    """prints the dictionary out by key and value in column format"""
    print("Here is the dictionary output in column format:")
    for key, value in dictionary.items():
        print(key+"\t", value)


def sort_it_out(a_dict):
    """makes dictionary into a list and sorts it by highest to lowest value"""
    dictionary_is_list = []
    for key, value in a_dict.items():
        dictionary_is_list.append([value, key])
    dictionary_is_list_final = sorted(dictionary_is_list)
    return dictionary_is_list_final


def main():
    dir = os.getcwd()
    # gets working directory aka the name of the directory the .py file is in
    step1 = make_a_list(os.path.join(dir, 'data.txt'))
    # os.join formats the dir name and file name so that it can be read by py
    step2 = list_to_dict(step1)
    print_it_pretty(step2)
    y = sort_it_out(step2)
    print("The best run is ", end="")
    print(y[0][1], end=" with a likeihood value of: ")
    # prints the highest list value index=1 (the equivalent of the key name)
    print(y[0][0], end=".")
    # prints the highest list value index=0 (the equivalent of the value)


if __name__ == '__main__':
    main()

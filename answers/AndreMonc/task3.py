# !/usr/bin/env python
# encoding: utf-8


"""
My text-editing program
Created by Andre Moncrieff on 29 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import operator
import collections
import re

my_data = open("ExaML.txt", "r")
list_of_lines = my_data.readlines()


def listify_run_names():
    run_names = []
    for line in list_of_lines:
        if re.search("ExaML_info", line):
            match = re.search(r"(.+)\\\\tL.", line)
            run_names.append(match.group(1))
    return run_names


def listify_log_likelihoods():
    log_likelihoods = []
    for line in list_of_lines:
        if re.search("ExaML_info", line):
            match = re.search(r".+\\t(-\w+\.\w+).+", line)
            log_likelihoods.append(match.group(1))
    return log_likelihoods


def make_dict(names, likes):
    diction = dict(zip(names, likes))
    return diction


def sorted_dict(raw_dictionary):
    sorted_dict = sorted(raw_dictionary.items(), key=lambda x: (x[1], x[0]))
    return sorted_dict


def best_function(names_likes_dict):
    highest_log = sorted(names_likes_dict.items(), key=lambda x: (x[1], x[0]))[:1]
    return highest_log


def main():
    the_run_names = listify_run_names()
    # print(the_run_names)
    log_likelihoods = listify_log_likelihoods()
    # print(log_likelihoods)
    the_dict = make_dict(the_run_names, log_likelihoods)
    print("\n\nUnordered dictionary output:\n")
    for key in the_dict:
        print(key + "\t" + str(the_dict[key]))
    sorted_dictionary = sorted_dict(the_dict)
    print("\n\nOrdered dictionary output (larger values to smaller values):\n")
    for item in sorted_dictionary:
        print(str(item[0]) + "\t" + str(item[1]))
    best = best_function(the_dict)
    print("\n\nThe maximum log-likelihood value is:\n")
    print(best[0][1])
    print("\n\n")


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 10
Task 3 Program: Using Dictionaries to Process ExaML Run Data
Jessie Salter
26 February 2016
"""

import re


def run_value(my_file):
    '''Reads input from a file and converts it to a string. Uses re to extract
    the run name and likelihood score and assigns these pairs to a dictionary.
    Prints the list of run names and corresponding scores.'''
    with open(my_file) as data:
        data_string = data.read()
        # Imports text as a string
        run_name = re.findall('ExaML_info.\w+', data_string)
        # Stores all run names in a list
        likelihood_score = re.findall('-\w+.\w+', data_string)
        # Store all likelihood scores in a list
        run_score = dict(zip(run_name, likelihood_score))
        # Creates a dictionary with run name as key, likelihood score as value
    for run, score in run_score.items():
        print(str(run).ljust(14), str(score).rjust(15))
        # Prints the run names and scores in two columns
    return run_score


def best_run(results):
    '''Using the dictionary created above, creates a list with each run/score
    pair as an entry. Sorts by score and prints the name and score of the best
    run.'''
    results_list = []
    for run, score in results.items():
        results_list.append([score, run])
        # Do it in this order so it sorts by score value, not run number
    sorted_results = sorted(results_list)
    print(
        'The best run is', sorted_results[0][1],
        'with a likelihood score of', sorted_results[0][0]+'.')


def main():
    results = run_value('rundata.txt')
    best_run(results)


if __name__ == '__main__':
    main()

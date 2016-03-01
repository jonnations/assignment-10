#!/usr/bin/env python

"""
Task 3:
Write a program that processess these data to create a dictionary that maps
the ExaML run name (e.g. ExaML_info.T6 as the key) to the ExaML log-likelihood
value (e.g. -82924194.67 as the value). Use this function or a function that
calls this function to prettily print the run name followed by the
log-likelihood value in two column format to the screen. Also write a function
that sorts the log-likelihood values and helps us determine which run name
maximizes the -log likelihood value (e.g. the run name having the value closest
to zero). Also output the name of this "best" run to the screen.

Created by Shraddha Shrestha on February 29, 2016
Copyright 2016. All rights reserved.

"""


def edit_string(string):
    step1 = string.replace("\t", " ").replace("Likelihood of best tree:", " ")
    step2 = step1.split()
    # getting key and value
    key = step2[::2]
    value = step2[1::2]
    edited_file = dict(zip(key, value))
    return edited_file


def store_edit(edited_file):
    for key, value in edited_file.items():
        print(key, "\t", value)


def sort_file(edited_file):
    new = []
    for key, value in edited_file.items():
        new.append((key, value))
        new.sort()
    print("Max log likelihood value is", new[0][1], "for ExaML run", new[0][0])


def main():
    string = """ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
ExaML_info.T5\tLikelihood of best tree:\t-82924194.71
ExaML_info.T9\tLikelihood of best tree:\t-82924194.73
ExaML_info.T7\tLikelihood of best tree:\t-82924252.98
ExaML_info.T2\tLikelihood of best tree:\t-82924253.01
ExaML_info.T1\tLikelihood of best tree:\t-82924354.95
ExaML_info.T8\tLikelihood of best tree:\t-82924354.98
ExaML_info.T15\tLikelihood of best tree:\t-82924366.58
ExaML_info.T0\tLikelihood of best tree:\t-82924366.59
ExaML_info.T4\tLikelihood of best tree:\t-82924397.48
ExaML_info.T16\tLikelihood of best tree:\t-82924424.87
ExaML_info.T3\tLikelihood of best tree:\t-82924424.89
ExaML_info.T14\tLikelihood of best tree:\t-82924426.52
ExaML_info.T12\tLikelihood of best tree:\t-82924426.53
ExaML_info.T13\tLikelihood of best tree:\t-82924426.54
ExaML_info.T19\tLikelihood of best tree:\t-82924465.57
ExaML_info.T17\tLikelihood of best tree:\t-82924707.69
ExaML_info.T10\tLikelihood of best tree:\t-82925366.65
ExaML_info.T18\tLikelihood of best tree:\t-82925393.89
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6 """
    new = edit_string(string)
    print(store_edit(new))
    sort_file(new)


if __name__ == '__main__':
    main()

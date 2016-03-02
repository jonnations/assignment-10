#!/usr/bin/env python
# utf-8

"""
Assignment 10,task3
Created by Pramod Pantha on March 1, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


def modified(string):
    """
    split the string by line ending,replaces the tab separations with commas
    remove the ,'', between two items in the list
    """
    modification1 = string.replace("\t", " ").replace("Likelihood of best tree:"
                , " ")
    modification2 = modification1.split()
    keys = modification2[::2]
    values = modification2[1::2]
    result = dict(zip(keys, values))
    return result


def print_keyvalue(result):
    for key, value in result.items():
        print(key, "\t", value)


def best_run(result):
    A = []
    for key, value in result.items():
        A.append((key, value))
        A.sort()
    print(
          "the maximum likelihood log value is", A[0][1], "for this run name"
          , A[0][0])


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
    A = modified(string)
    print_keyvalue(A)
    best_run(A)


if __name__ == '__main__':
    main()

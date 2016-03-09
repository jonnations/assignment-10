#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 10

Task 3

This program processes ExaML data and prints the run name followed
by the log-likelihood value.  It also prints the run name of the
"best" run which maximizes the log-likelihood value.

Elisa Elizondo
"""

string = "ExaML_info.T6\tLikelihood of best tree:\t-82924194.67\n\
ExaML_info.T5\tLikelihood of best tree:\t-82924194.71\n\
ExaML_info.T9\tLikelihood of best tree:\t-82924194.73\n\
ExaML_info.T7\tLikelihood of best tree:\t-82924252.98\n\
ExaML_info.T2\tLikelihood of best tree:\t-82924253.01\n\
ExaML_info.T1\tLikelihood of best tree:\t-82924354.95\n\
ExaML_info.T8\tLikelihood of best tree:\t-82924354.98\n\
ExaML_info.T15\tLikelihood of best tree:\t-82924366.58\n\
ExaML_info.T0\tLikelihood of best tree:\t-82924366.59\n\
ExaML_info.T4\tLikelihood of best tree:\t-82924397.48\n\
ExaML_info.T16\tLikelihood of best tree:\t-82924424.87\n\
ExaML_info.T3\tLikelihood of best tree:\t-82924424.89\n\
ExaML_info.T14\tLikelihood of best tree:\t-82924426.52\n\
ExaML_info.T12\tLikelihood of best tree:\t-82924426.53\n\
ExaML_info.T13\tLikelihood of best tree:\t-82924426.54\n\
ExaML_info.T19\tLikelihood of best tree:\t-82924465.57\n\
ExaML_info.T17\tLikelihood of best tree:\t-82924707.69\n\
ExaML_info.T10\tLikelihood of best tree:\t-82925366.65\n\
ExaML_info.T18\tLikelihood of best tree:\t-82925393.89\n\
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6"

def alter_string(string):
    string2 = string.replace('\t', '')
    string3 = string2.replace('Likelihood of best tree:', ',')
    string4 = string3.split('\n')
    return(string4)

def make_dict(string4):
    list1 = []
    for info in string4:
        string5 = info.split(',')
        list1.append(string5)

    dict1 = {}
    for info in list1:
        dict1[info[0]] = info[1]
    return dict1

def best_run(dict1):
    list2 = []
    for key, value in sorted(dict1.items(), key=lambda x: x[1], reverse=True):
        list2.append([key, value])
    best = ' '.join(list2[19])
    return best

def main():
    string4 = alter_string(string)
    dict1 = make_dict(string4)
    list3 = []
    for key, value in dict1.items():
        print(key, value)
    best = best_run(dict1)
    print("The maximized run is:", best[:14])


if __name__ == '__main__':
    main()

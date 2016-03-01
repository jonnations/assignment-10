#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 10

Created by Michael Henson on 29 February 2016.
Copyright 2016 Michael W Henson. All rights reserved.
"""

import operator

def part1(string):
    '''
    http://www.tutorialspoint.com/python/python_dictionary.htm
    http://stackoverflow.com/questions/13054483/add-key-value-pairs-to-a-python-dictionary
    '''
    code = string.replace('Likelihood of best tree:\t', ' ').replace('\t', '\n').split('\n')
    my_dict = dict(zip(code[2::2], code[3::2]))
    return(my_dict)


def part2(my_dict):
    for key, value in my_dict.items():
        print(key, '\t', value)


def part3(my_dict):
    '''
http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
http://stackoverflow.com/questions/13054483/add-key-value-pairs-to-a-python-dictionary
http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
    '''
    top = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)[:1]
    print(top)

def main():
    my_string = """
ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
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
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6"""
    my_dict = part1(my_string)
    print("\nAnswer to part 2; listed")
    part2(my_dict)
    print("\nAnswer to part 3; ordered")
    print("This is the best:")
    part3(my_dict)

if __name__ == '__main__':
    main()

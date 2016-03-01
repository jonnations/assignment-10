#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 10, Task 3
Austen T. Webber
2016_2_29
"""

import operator

def vols1(string):
    code = string.replace('Likelihood of best tree:\t', ' ').replace(
        '\t', '\n').split('\n')
    my_dic = dict(zip(code[2::2], code[3::2]))
    return(my_dic)


def vols2(my_dic):
    for key, value in my_dic.items():
        print(key, '\t', value)


def vols3(my_dic):
    top = sorted(my_dic.items(), key=operator.itemgetter(1), reverse=True)[:1]
    print(top)

def main():
    examl = """
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
    my_dic = vols1(examl)
    vols2(my_dic)
    print("Best Run:")
    vols3(my_dic)

if __name__ == '__main__':
    main()


# http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
# http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
# http://stackoverflow.com/questions/13054483/add-key-value-pairs-to-a-python-dictionary

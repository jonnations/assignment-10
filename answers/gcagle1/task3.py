#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
22 Feb 2016
Assignment 10 Task 3

A program that creats a dictionary that maps ExaML run name to ExaML
log-likelihood value and prints in descending order.
Also displays "best" (least negative) run.
http://stackoverflow.com/questions/4627981/creating-a-dictionary-from-a-string
'''
my_data = '''

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
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6
'''


def clean_my_data(d=my_data):
    replace_data = d.replace('\n', '\t')
    split_data = replace_data.split('\t')
    join_data = ','.join(split_data)
    clean1 = join_data.lstrip(',,')
    clean_data = clean1.rstrip(',')
    return clean_data


def make_examl_dict(s=clean_my_data):
    string2 = s.replace(',Likelihood of best tree:,', '\t')
    examl_dict = dict((k, float(v)) for k, v in (e.split('\t') for e in
    string2.split(',')))
    return examl_dict


def get_results(examl_dict):
    '''makes a tuple of the examl results and sorts low to high'''
    t = []
    for key, value in examl_dict.items():
        t.append((value, key))
    t.sort(reverse=True)
    print('EXaML Results:')
    for freq, word in t:
        print(word, freq, sep='\t')
    print('The best run is:')
    for freq, word in t[:1]:
        print(word, freq, sep='\t')


def main():
    get_results(make_examl_dict(clean_my_data()))

if __name__ == '__main__':
    main()

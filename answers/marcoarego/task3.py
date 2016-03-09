# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 20:46:36 2016

@author: Marco
"""
'''
Task 3

Write a program that processess these data to create a dictionary that maps 
the ExaML run name (e.g. ExaML_info.T6 as the key) to the ExaML log-likelihood 
value (e.g. -82924194.67 as the value). Use this function or a function that 
calls this function to prettily print the run name followed by the 
log-likelihood value in two column format to the screen like so

ExaML_info.T6   -82924194.67
ExaML_info.T5   -82924194.71

Also write a function that sorts the log-likelihood values and helps us 
determine which run name maximizes the -log likelihood value (e.g. the run 
name having the value closest to zero). Also output the name of this "best" 
run to the screen.
'''

# importing modules
import re

# Global Variable
EXAML = (
'''ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
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
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6'''
)


def get_examl(examl):
    '''
    This function uses regex to search and capture the desired portions of
    the ExaML entries
    '''
    lista = examl.split("\n")
    entries = []
    logs = []
    for info in lista:
        # Capturing the first part
        begin = re.search('(\w*_\w*\.T\d*)',info).group(1)
        # capturing the last part        
        end = re.search('(-\d*\.\d*)',info).group(1)
        entries.append(begin)
        logs.append(end)
    dictionary = dict(zip(entries,logs))
    return dictionary


def dict_reversor(my_dict):
    '''
    this function will create a list of lists. The first value of each list
    correspond the dictionary values while the second value of the list
    correspond to the dictionary keys. So, I am just reversing the dictionary
    in a way that I am not loosing any repeated value.
    '''
    keys = []
    values = []    
    for key, value in my_dict.items():
        keys.append(key)
        values.append(value)
    result = list(zip(values,keys))
    # Sorting the list
    sort = sorted(result, reverse = False)    
    return sort


def main(examl):
    dictionary = get_examl(examl)    
    final_list = dict_reversor(dictionary)
    for x,y in final_list:
        print(y+':\t'+str(x))
    best_entry = final_list[0][1]
    best_log = str(final_list[0][0])
    print("\n\nThe best run is: {0}, with the log value of {1}".format(best_entry, best_log))
    
    
if __name__ == '__main__':
    main(EXAML)
        
    
        
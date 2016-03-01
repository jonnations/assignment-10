#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Mar 1, 2016
Write a program that processess the given data to create a
dictionary that maps the ExaML run name (e.g. ExaML_info.T6 as the key) to the
ExaML log-likelihood value (e.g. -82924194.67 as the value). Use this function
or a function that calls this function to prettily print the run name followed
by the log-likelihood value in two column format to the screen. Also include a
function that sorts the log-likelihood values and helps us determine which run
name minimizes the negative log likelihood value (e.g. the run name having the
LL value closest to zero). Also output the name of this "best" run to the
screen. 
@author: York
'''
import re


def remove_empty_lines():
    data = """ExaML_info.T6\tLikelihood of best tree:\t-82924194.67\n
            ExaML_info.T5\tLikelihood of best tree:\t-82924194.71\n
            ExaML_info.T9\tLikelihood of best tree:\t-82924194.73\n
            ExaML_info.T7\tLikelihood of best tree:\t-82924252.98\n
            ExaML_info.T2\tLikelihood of best tree:\t-82924253.01\n
            ExaML_info.T1\tLikelihood of best tree:\t-82924354.95\n
            ExaML_info.T8\tLikelihood of best tree:\t-82924354.98\n
            ExaML_info.T15\tLikelihood of best tree:\t-82924366.58\n
            ExaML_info.T0\tLikelihood of best tree:\t-82924366.59\n
            ExaML_info.T4\tLikelihood of best tree:\t-82924397.48\n
            ExaML_info.T16\tLikelihood of best tree:\t-82924424.87\n
            ExaML_info.T3\tLikelihood of best tree:\t-82924424.89\n
            ExaML_info.T14\tLikelihood of best tree:\t-82924426.52\n
            ExaML_info.T12\tLikelihood of best tree:\t-82924426.53\n
            ExaML_info.T13\tLikelihood of best tree:\t-82924426.54\n
            ExaML_info.T19\tLikelihood of best tree:\t-82924465.57\n
            ExaML_info.T17\tLikelihood of best tree:\t-82924707.69\n
            ExaML_info.T10\tLikelihood of best tree:\t-82925366.65\n
            ExaML_info.T18\tLikelihood of best tree:\t-82925393.89\n
            ExaML_info.T11\tLikelihood of best tree:\t-82925447.6\n"""

    replace_tab = data.replace("\t", ",")
    return re.sub("\n\s*\n*", "\n", replace_tab)


def function1():
    result = remove_empty_lines()
    list=result.split("\n")
    print(list)
    delimiter=','
    c=delimiter.join(list)
    print(c)
    list2=c.split(",")
    print(list2)
    for item in list2:
        list3=list2.remove('Likelihood of best tree:')
        print(list2)
    return(list2)


def main():
 
   function1()
   
  

if __name__ == '__main__':
    main()
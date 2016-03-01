#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 20:25:43 2016

@author: Glaucia
"""
"""
Task 3
Here are the same data from ExaML that you've seen before, although they are a little cleaner this time:

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

Write a program that processess these data to create a dictionary that maps 
the ExaML run name (e.g. ExaML_info.T6 as the key) to the ExaML log-likelihood value 
(e.g. -82924194.67 as the value). Use this function or a function that calls this function 
to prettily print the run name followed by the log-likelihood value in two column format
to the screen like so:

ExaML_info.T6   -82924194.67
ExaML_info.T5   -82924194.71

Also write a function that sorts the log-likelihood values and helps us determine which
run name maximizes the -log likelihood value (e.g. the run name having the value closest to zero). 
Also output the name of this "best" run to the screen.

"""
import re

def dictExaML(ExaMLstring):
    """prints out the run name and likelihood in tow columns and returns a dictionary"""
    #splitting the ExaML string into list
    ExaMLList = ExaMLstring.split("\n")
    #empty list to store the name of the sequnece
    runname=[] 
    #empty list to store log likelihoods
    loglikelihood=[]
    #iterating across sequences in the ExaMLlist
    for run in ExaMLList:
        #excluding None objects
        if run != "": 
            #doing regex to select blocks of text
            matchObj = re.match( r'(.*)\t.*\t(.*)', run, re.M|re.I)
            #appending run name to a list
            runname.append(matchObj.group(1))
            #appending loglikelihood to another list
            loglikelihood.append(matchObj.group(2))
        else:
            pass
    #zipping run names and log likelihoods in a dictionary
    dictionary=dict(zip(runname,loglikelihood))
    #empty list to store values of the dictionary in a list
    dictlist=[]  
    for key, value in dictionary.items():
        newlist = [value,key]
        dictlist.append(newlist)
    print("Two columns:")
    #printing the elements of the list in two columns
    for lis in dictlist:
        print(lis[1],"\t",lis[0])
    return dictionary

    
def sortloglikelihood(dic):
    """sorts the likelihood in the dictionary, prints the sorted list and prints the best run name"""
    dictlist=[]
    #iterating across values in a dictionary
    for key, value in dic.items():
        newlist = [key,value]
        dictlist.append(newlist)
    #sorting a list of lists which store the run names and likelihoods
    listoflists=(sorted(dictlist, key=lambda dictlist: dictlist[1],reverse=False)) 
    #printing the sorted likelihoods
    print("Sorted likelihoods:")
    for lis in listoflists:
        print(lis[0],":",lis[1])
    #printing the best run name
    print("Best run name: " + listoflists[0][0])


def main():
    Brantstring="""ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
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
    dicttodeal=dictExaML(Brantstring)
    sortloglikelihood(dic=dicttodeal)
    
    
if __name__ == '__main__':
    main()   


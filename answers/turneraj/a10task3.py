#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 10 that sorts ExaML runs by log likelihood (LL) values, with the best LL (closest to zero) printed first. The name of the best run and its associated LL is printed out after the sort list or runs.
 
 Created by A.J. Turner on February 28, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""


def my_runs(examl):
	"""function takes log likelihood and matches it with its repsective run"""
	runs = examl.replace("\n", "").split("\t")
	#zip together every first and third item in entire list into a dictionary
	return dict(zip(runs[0::3], runs[2::3]))


def best_value(run_dict):
	"""function that sorts the dictionary and also finds the log likelihood (LL) value closest to zero"""
	#sorts dictionary key/value by LL with LL closest to zero as first 
	sorted_runs = sorted(run_dict.items(), key=lambda item: -item[1])  
	#gets the run/LL pair with LL value closest to zero
	maximum = max(run_dict, key=run_dict.get) 
	return sorted_runs, maximum, run_dict[maximum]


def main():
	examl = """ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
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
	
	run_dict = my_runs(examl)
	for key,value in run_dict.items():
		run_dict[key] = float(run_dict[key]) #making every value in key/value a float

	#unpacking returned values from func 2
	compare_runs, maximum_key, maximum_value = best_value(run_dict) 
	for items in compare_runs:
		print(items[0],"\t",items[1]) #prints items in nested list at zero index and 1 (key/value)
	print("\n""Best: ", maximum_key, maximum_value) #printing best run and associated LL 


if __name__ == '__main__':
	main()

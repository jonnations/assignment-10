#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 10 that identifies word usage in text through the use of a standard dictionary. The program will tally up the top ten words in text (sentence/paragraph, etc) and return them with their usage in decreasing order. Words are the keys and their respective value is their count. 

 Created by A.J. Turner on February 29, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""


def word_count(string):
	my_words = string.lower().replace("\n", " ").replace("  ", " ").replace("'", "").replace(",", ""). replace("\t", "").replace (".", "").split(" ")
	#print(my_words) to check formatting of text
	my_dict = {} #placeholder for creating dictionary
	#iterate over items to give words(key) with count (value)
	for item in my_words:
		if item in my_dict: #checking for key in dictionary
			my_dict[item] += 1 #if in dictionary, add 1 to value
		else: #if word isn't in dictionary originally, create as new key and make value 1
			my_dict[item] = 1
	return my_dict


def top_ten(dict):
	"""#accessed below steps from http://stackoverflow.com/questions/4088265/sorted-word-frequency-count-using-python"""
	sorted_dict = sorted(dict.items(), key=lambda item: -item[1])
	return sorted_dict[0:10]


def main():
	string = """Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

	After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

	The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

	Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

	But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end."""
	

	dict = word_count(string)
	my_list = top_ten(dict)
	print("The top ten words:\n")
	for items in my_list:
		print(items[0],"\t",items[1]) #prints items in tuple at zero index and 1 (key/value pairs)


if __name__ == '__main__':
	main()
	

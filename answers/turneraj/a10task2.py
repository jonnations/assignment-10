#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 10 that uses the counter function to tally up the top ten words in text (sentence/paragraph, etc) and returns them with their usage in decreasing order.  

 Created by A.J. Turner on February 28, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""

from collections import Counter


def easy_count(string):
	#get rid of all punctuation, make letters lowercase
	text_in = string.lower().replace("\n", " ").replace("  ", " ").replace("'", "").replace(",", ""). replace("\t", "").replace (".", "").split(" ")
	#print(text_in) to check formatting before using Counter
	count_it = Counter(text_in).most_common(10)
	return count_it


def main():
	string = """Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

	After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

	The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

	Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

	But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end."""
	
	my_result = easy_count(string)
	print("The top then words:\n")
	for item in my_result:
		print(item[0],"\t",item[1]) #prints items in tuple at zero index and 1 (key/value pairs)

	
if __name__ == '__main__':
	main()

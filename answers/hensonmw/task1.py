#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 10

Created by Michael Henson on 29 February 2016.
Copyright 2016 Michael W Henson. All rights reserved.
"""


def word_count(string):
	'''
	http://stackoverflow.com/questions/28725503/count-word-frequency-in-a-txt-file-using-only-dictionary-python-3
	http://stackoverflow.com/questions/16557900/how-to-convert-string-to-dictionary-and-count-the-number-of-each-word
	http://programminghistorian.org/lessons/counting-frequencies
	'''
	my_words = string.lower().replace('  ', ' ').replace(',', '').replace(".", "").split(" ")
	my_dict = {}
	for item in my_words:
		if item in my_dict:
			my_dict[item] += 1
		else:
			my_dict[item] = 1
	return my_dict


def top_words(counts):
	sorted_dict = sorted(counts.items(), key=lambda item: -item[1])
	return sorted_dict[0:10]


def main():

	my_string = """Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.
	After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.
	The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.
	Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.
	But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end."""

	counts = word_count(my_string)
	my_list = top_words(counts)
	for items in my_list:
		print(items[0],"\t",items[1])


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 10, Task 1
Austen T. Webber
2016_2_29
"""


def star_count(string):
	words = string.lower().replace('  ', ' ').replace(',', '').replace(".", "").split(" ")
	my_dictionary = {}
	for item in words:
		if item in my_dictionary:
			my_dictionary[item] += 1
		else:
			my_dictionary[item] = 1
	return my_dictionary


def top_words(counts):
	sort_dic = sorted(counts.items(), key=lambda item: -item[1])
	return sort_dic[0:10]


def main():

	epic_string = """Stars burn a very light type of air that is packed very
    tight in the middle of the star. The tiny pieces of the air join to form a
    slightly heavier type of air that can't burn in the star without the middle
    being much hotter and tighter. After a long time, all the very light air in
    the middle is used up. Then the star gets much hotter and tighter in the
    middle, so it can burn the slightly heavier air. It also also gets much
    bigger and cooler outside. But it is still so hot it will burn up any
    close-in worlds. The sun is a star and will do this after a very long time.
    It will get so big that it will burn our world all up. This will not happen
    for at least ten hundred hundred hundred hundred years, so we don't have
    to worry about it now. Long after that, a star like the sun will burn up
    all the slightly heavier air, too. Then it will become very tiny and hot
    and white, but will be so tiny it won't be able to keep its worlds warm.
    It will keep cooling off over a very very long time. The worlds that are
    left will be all ice. But stars that are heavier can go on to burn heavier
    and heavier things, until finally they make the biggest flash we know.
    That is their end."""

	counts = star_count(epic_string)
	final_list = top_words(counts)
	for items in final_list:
		print(items[0],"\t",items[1])


if __name__ == '__main__':
    main()

# http://stackoverflow.com/questions/28725503/count-word-frequency-in-a-txt-file-using-only-dictionary-python-3
# http://stackoverflow.com/questions/16557900/how-to-convert-string-to-dictionary-and-count-the-number-of-each-word

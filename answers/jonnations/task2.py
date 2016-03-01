#!/usr/bin/env python
# utf-8

"""
Assignment 10, Task 2
Jon Nations on 29 February 2016
Code modifed from count_words.py from https://gist.github.com/bradmontgomery
"""

from collections import Counter
import re


def main(n=10):


    stars = "Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds. The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now. Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice. But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end."

    # reorganize the paragraph
    stars = re.sub('\s+', ' ', stars)  # condense all whitespace
    stars = re.sub('[^A-Za-z ]+', '', stars)  # remove non-alpha chars
    # regular expressions from gist.github.com/bradmontgomery
    star_list = stars.split()

    # counts the words
    star_count = Counter(star_list)

    # Prints the top 10 words
    print("The Top {0} words".format(n))
    for word, count in star_count.most_common(n):
        print("{0}: {1}".format(word, count))


if __name__ == "__main__":
    main()

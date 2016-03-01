# !/usr/bin/env python
# encoding: utf-8


"""
My counter program
Created by Andre Moncrieff on 29 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


from collections import Counter


quote = """Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.

After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.

The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.

Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.

But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end."""


def cleanup(quotatian):
    cleaned_quote_0 = quote.lower()
    cleaned_quote_1 = cleaned_quote_0.replace(".", "").replace(",", "")
    cleaned_quote_2 = cleaned_quote_1.replace("\n\n", " ")
    return cleaned_quote_2


def makelist(parsed_quote):
    parsed = parsed_quote.split(" ")
    return parsed


def make_dict(quote_as_list):
    synthesis_dict = Counter(quote_as_list)
    return synthesis_dict


def top_ten_words(the_dict):
    top_ten = the_dict.most_common(10)
    return top_ten


def main():
    cleaned_quote = cleanup(quote)
    #print(cleaned_quote)
    quote_as_list = makelist(cleaned_quote)
    #print(quote_as_list)
    word_count_dict = make_dict(quote_as_list)
    #print(word_count_dict)
    top_ten = top_ten_words(word_count_dict)
    print("\n\nThe ten most common words in the dictionary and their word counts:\n")
    for item in top_ten:
        print(item[0] + "\t" + str(item[1]))
    print("\n\n")

if __name__ == '__main__':
    main()

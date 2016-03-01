#! /usr/bin/env python
# encoding UTF-8

'''
Assignment10Task2 biol7800
ZacCarver 03/01/2016
Process the given ExaML data using a dictionary. Print this cleaned data in a
'pretty' format.
'''

import re
import operator


def run(f):
    # allows the file to be read as string
    data = f.read()
    # finds and keeps quoted bit
    r = re.findall('ExaML_info.\w+', data)
    s = re.findall('-w+.\w+', data)
    # zips it up into dictionary form
    rs_dict = dict(zip(r, s))
    for r, s in rs_dict.items():
        # causes the field between to be a min number of chars wide.
        # docs.python.org/3.0/tutorial/inputoutput.html
        print('{0:10}    {1:10d}'.format(r, s))
    return rs_dict


def b(rs_dict):
    # sorts in the same manner as in previous tasks
    bestrs = sorted(rs_dict.items(), key=operator.itemgetter(1), reverse=True[-1:])
    print('best', bestrs)


def main():
    f = open('ExaML10.txt', 'r')
    rs_dict = run(f)
    b(rs_dict)

if __name__ == '__main__':
    main()

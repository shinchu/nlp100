#! /usr/bin/env python
# coding: utf-8
# nlp100_2.py
# 2020-06-06
#

import argparse
import csv
from itertools import islice


def line_number(file):
    return sum([1 for _ in open(file, 'r')])


def sec10(file):
    print(line_number(file))


def sec11(file):
    with open(file, 'r') as f:
        for l in f:
            print(l.replace("\t", " "), end="")


def sec12(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        rows = [row for row in reader]

    # transpose
    cols = [list(x) for x in zip(*rows)]

    with open('../data/col1.txt', 'w') as f:
        f.write('\n'.join(cols[0]))

    with open('../data/col2.txt', 'w') as f:
        f.write('\n'.join(cols[1]))


def sec13():
    with open('../data/col1.txt', 'r') as f:
        col1 = f.read().splitlines()

    with(open('../data/col2.txt', 'r')) as f:
        col2 = f.read().splitlines()

    col12 = []
    for n, g in zip(col1, col2):
        col12.append(f"{n}\t{g}")

    with open('../data/col12.txt', 'w') as f:
        f.write('\n'.join(col12))


def sec14(file, n):
    with open(file, 'r') as f:
        head = list(islice(f, n))

    for line in head:
        print(line, end="")


def sec15(file, n):
    n_line = line_number(file)
    print(n_line - n)

    with open(file, 'r') as f:
        head = list(islice(f, n_line - n, n_line))

    for line in head:
        print(line, end="")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("section", help="section number", type=int)
    parser.add_argument("file", help="filepath")
    parser.add_argument("-n", "--number", help="number of lines", type=int)

    args = parser.parse_args()
    sec = args.section
    file = args.file

    if sec == 10:
        sec10(file)
    elif sec == 11:
        sec11(file)
    elif sec == 12:
        sec12(file)
    elif sec == 13:
        sec13()
    elif sec == 14:
        n = args.number
        sec14(file, n)
    elif sec == 15:
        n = args.number
        sec15(file, n)
    else:
        print("Please specify a number between 10 and 19.")
        exit()

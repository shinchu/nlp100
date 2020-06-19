#! /usr/bin/env python
# coding: utf-8
# nlp100_2.py
# 2020-06-06
#

import argparse
import os
import math
import csv
import operator
from itertools import islice
from collections import Counter


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


def sec14(file, n=10):
    with open(file, 'r') as f:
        head = list(islice(f, n))

    for line in head:
        print(line, end="")


def sec15(file, n=10):
    n_line = line_number(file)
    print(n_line - n)

    with open(file, 'r') as f:
        head = list(islice(f, n_line - n, n_line))

    for line in head:
        print(line, end="")


def sec16(file, n=2):
    n_line = line_number(file)
    split_lines = math.ceil(n_line / n)

    out_file = f"{os.path.dirname(file)}/{os.path.basename(file).split('.')[0]}"

    for i in range(n):
        with open(file, 'r') as f:
            with open(f"{out_file}_{i+1}.txt", 'w') as f_out:
                if i == n - 1:
                    f_out.write("".join(list(islice(f, i * split_lines, None))))
                else:
                    f_out.write("".join(list(islice(f, i * split_lines, i * split_lines + split_lines))))


def sec17(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        rows = [row for row in reader]

    # transpose
    cols = [list(x) for x in zip(*rows)]

    print('\n'.join(set(cols[0])))


def sec18(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        rows = [row for row in reader]

        for row in rows:
            row[2] = int(row[2])
            row[3] = int(row[3])

        for line in sorted(rows, key=operator.itemgetter(2), reverse=True):
            print(f'{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}')


def sec19(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        rows = [row for row in reader]

    # transpose
    cols = [list(x) for x in zip(*rows)]

    counter = Counter(list(cols[0]))

    for name, count in counter.most_common():
        print(f'{count} {name}')


if __name__ == "__main__":
    """
    Run as:
    python nlp100_2.py 15 ../data/*.txt [-n 16]
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("section", help="section number", type=int)
    parser.add_argument("file", help="filepath")
    parser.add_argument("-n", "--number", help="number of lines/divided files", type=int)

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
    elif sec == 16:
        n = args.number
        sec16(file, n)
    elif sec == 17:
        sec17(file)
    elif sec == 18:
        sec18(file)
    elif sec == 19:
        sec19(file)
    else:
        print("Please specify a number between 10 and 19.")
        exit()

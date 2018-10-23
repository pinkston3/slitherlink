#!/usr/bin/python

import requests
from bs4 import BeautifulSoup


def get_puzzle(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    puzzle_table = soup.find('table', id='LoopTable')

    puzzle_rows = puzzle_table.findAll('tr')
    puzzle_rows = puzzle_rows[1::2]

    row_specs = []

    for row in puzzle_rows:
        puzzle_cols = row.findAll('td')
        puzzle_cols = puzzle_cols[1::2]

        row_spec = ''

        for col in puzzle_cols:
            cellval = col.string
            if not cellval:
                cellval = ' '
            row_spec += cellval

        row_specs.append(row_spec)

    print("%d %d" % (len(row_specs), len(row_specs[0])))
    print('\n'.join(row_specs))


# Only works against the "old version" of the website, since the new version
# uses client-side Javascript to download and display the puzzle.  The "size"
# argument doesn't specify the actual puzzle size; rather, it maps to one of
# a number of sizes and difficulties.  Note that 'normal' puzzles can be solved
# by repeated rule-application, but 'hard' puzzles also require guessing.
#
# [no size] = 5x5 normal
#         4 = 5x5 hard
#        10 = 7x7 normal
#        11 = 7x7 hard
#         1 = 10x10 normal
#         5 = 10x10 hard
#         2 = 15x15 normal
#         6 = 15x15 hard
#         3 = 20x20 normal
#         7 = 20x20 hard
#         8 = 25x30 normal
#         9 = 25x30 hard
#        13 = special daily loop
#        12 = special weekly loop
#        14 = special monthly loop

get_puzzle('http://www.puzzle-loop.com/?v=0&size=5')


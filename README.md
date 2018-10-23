# Slitherlink Solver

For a while I was addicted to the game Slither Link
(https://www.puzzle-loop.com/).  In an effort to get over it, I went
ahead and wrote a solver that could solve these game in an automated
manner.  This project is the result of that effort.

The code isn't particularly pretty, but it is definitely able to solve
these puzzles.  In many cases, one can apply a very simple set of rules
over and over again, until the game is solved.  In situations where the
set of rules is insufficient to solve the puzzle, random moves can be
made to see if a solution will be found.

I am mostly sick of this game by now, so it seems to have been a successful
approach to getting over it.

## Getting Puzzles

In order to get puzzles to solve, I also wrote a program to download the
puzzle data from https://www.puzzle-loop.com into a simple file format.
The program is called `get_puzzle.py`, and can be edited to download
puzzles of various sizes.  Read the comments in this short program to see
what values to specify.  To store the puzzle data, you can run something
like this:

        python get_puzzle.py > 10x10_hard_1.txt

Note:  To get this program to run, you must have the Python
[Requests](http://docs.python-requests.org/en/master/) and
[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
libraries installed.  I usually set up a virtual environment to do this.

        virtualenv venv
        source venv/bin/activate
        pip install requests
        pip install beautifulsoup4

## Puzzle Format

Here is an example 15x15 puzzle:

    15 15
     122 32 2    13
      22  222    3 
       311  1   122
     3  31  2   1  
    202  1 113 2222
       21 3221 1  3
    1 2     2 3  2 
    3   21 2    23 
      1    213 3  3
     32    12212  2
    3  3 122 2 2  3
     1    22 2   3 
    3    2 1   2023
    22 2  32  2    
    3   21    231 3

The first line contains the width and height of the puzzle; the remaining
lines contain the numbers that go into each cell of the puzzle, or a space
for no number.

The `puzzles` folder contains many such puzzles.  The naming convention
tends to be that "normal" puzzles are able to be solved entirely by repeated
application of the rules, and "hard" puzzles require guessing at various
points because the rules are insufficient.

## Running the Solver

The solver is called `slsolve.py`.  Currently it doesn't parse command line
arguments, so it is only configurable via editing the code.  To run the
program on a puzzle, do the following:

        python slsolve.py 10x10_hard_1.txt

The program will commence solving the puzzle, attempting to apply its rules
for solving until the board no longer changes, and then switching to a
random search mechanism.  Eventually, the program will print out the solution
to the puzzle once it is found.

## Issues

Here are the current known issues with the program.

*   Infrequently, the program crashes with a failed assertion.  It is unclear
    what is causing this failure, but I will probably eventually track it
    down and fix it.

*   As mentioned above, the solver doesn't take any command-line options, and
    it would be nice to have options like verbose output.

*   A far more interesting question is, how to generate hard slitherlink
    puzzles?  This is a topic worth exploring in the future!


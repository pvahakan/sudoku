#!/usr/bin/env python3

import numpy as np
import random



def read_data(path):
    """
    Reads data for sudoku from file.
    """
    data = np.zeros((9,9))
    scratch = []

    # Read data from .txt file to program memory
    with open(path) as datafile:
        content = datafile.readlines()
        for row in content:
            scratch.append(row.split())

    # Parse data to numpy array
    for i in  range(9):
        for j in range(9):
            try:
                data[i][j] = int(scratch[i][j])
            except ValueError:
                print("ValueError", scratch[i][j])

    return data



def console_print(ar):
    """
    Prints sudoku board to the console.

    :param ar: An array, the board
    """
    i, j = 0, 0
    for i in range(9):
        for j in range(9):
            if j == 2 or j == 5:
                print(int(ar[i][j]), "| ", end="")
            else:
                print(int(ar[i][j]), "  ", end="")
        if i == 2 or i == 5:
            print("\n---------------------------------")
        else:
            print()


def move(t, x1, y1, z1):
    cube[t[0]][t[1]][t[2]] += 1
    cube[t[0]][y1][z1] += 1
    cube[x1][y1][t[2]] += 1
    cube[x1][t[1]][z1] += 1
    cube[t[0]][t[1]][z1] -= 1
    cube[t[0]][y1][t[2]] -= 1
    cube[x1][t[1]][t[2]] -= 1
    cube[x1][y1][z1] -= 1


if __name__ == "__main__":
    # Paths to sudoku and its solution
    easy_sudoku = "./sudokus/s10a.txt"
    easy_sudoku_sol = "./solutions/s10a_s.txt"

    sudoku = read_data(easy_sudoku)
    console_print(sudoku)

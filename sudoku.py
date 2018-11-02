#!/usr/bin/env python3

import numpy as np

def console_print(ar):
    """
    Prints sudoku board to the console.

    :param ar: An array, the board
    """
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

if __name__ == "__main__":
    ar = np.zeros((9,9))
    console_print(ar)

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


def subsquares(sudoku):
    """
    Finds 9 subsquares of sudoku.

    :param sudoku: A numpy array, original sudoku.
    :return subsq: A list of 3x3 subarrays.
    """
    subsq = []
    midpoints = [(1,1), (1,4), (1,7),
                 (4,1), (4,4), (4,7),
                 (7,1), (7,4), (7,7)]

    for mp in midpoints:
        subsq.append(sudoku[ mp[0]-1:mp[0]+2, mp[1]-1:mp[1]+2 ])

    return subsq


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


class SudokuBoard():
    def __init__(self, board):
        self.board = board

    def print_board(self):
        i, j = 0, 0
        for i in range(9):
            for j in range(9):
                if j == 2 or j == 5:
                    print(int(self.board[i][j]), "| ", end="")
                else:
                    print(int(self.board[i][j]), "  ", end="")
            if i == 2 or i == 5:
                print("\n---------------------------------")
            else:
                print()

    def row(self, row : int):
        """
        Returns row'th row of board as an array.
        """
        return self.board[row]

    def column(self, col : int):
        """
        Returns col'th column of board as an array.
        """
        column = np.array([])
        for i in range(9):
            column = np.append(column, self.board[i][col])

        return column

    def subsquare(self, i : int, j : int):
        """
        Returns 3x3 array, which is a subsquare that contains a number in (i, j).
        """
        midpoints = [(1,1), (1,4), (1,7),
                    (4,1), (4,4), (4,7),
                    (7,1), (7,4), (7,7)]
        # 1. subsquare
        if i <= 2 and j <= 2:
            mp = midpoints[0]
        # 2. subsquare
        elif i <= 2 and 2 < j <= 5:
            mp = midpoints[1]
        # 3. subsquare
        elif i <= 2 and 5 < j <= 8:
            mp = midpoints[2]
        # 4. subsquare
        elif 2 < i <= 5 and j <= 2:
            mp = midpoints [3]
        # 5. subsquare
        elif 2 < i <= 5 and 2 < j <= 5:
            mp = midpoints [4]
        # 6. subsquare
        elif 2 < i <= 5 and 5 < j <= 8:
            mp = midpoints [5]
        # 7. subsquare
        elif 5 < i <= 8 and j <= 2:
            mp = midpoints [6]
        # 8. subsquare
        elif 5 < i <= 8 and 2 < j <= 5:
            mp = midpoints [7]
        # 9. subsquare
        elif 5 < i <= 8 and 5 < j <= 8:
            mp = midpoints [8]

        sbsquare = self.board[ mp[0]-1:mp[0]+2, mp[1]-1:mp[1]+2 ]

        return sbsquare

    def insert(self, num : int, i : int, j : int):
        """
        Inserts num to (i, j) in sudoku board.
        """
        if 0 < num <= 9:
            self.board[i][j] = num


if __name__ == "__main__":
    # Paths to sudoku and its solution
    easy_sudoku = "./sudokus/s10a.txt"
    easy_sudoku_sol = "./solutions/s10a_s.txt"

    sudoku = SudokuBoard(read_data(easy_sudoku))
    sudoku.print_board()


    # sudoku = read_data(easy_sudoku)
    # console_print(sudoku)
    # subsq = subsquares(sudoku)
    # print(subsq)

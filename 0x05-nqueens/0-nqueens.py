#!/usr/bin/python3
"""Nqueens Problem"""
import sys


board = []
positions = []


def solutions():
    """Returns the solution"""
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                positions[row][1] = col

    return positions


def backtrack(row, num, col, pos_diag, neg_diag):
    """
    Performs the backtracking algorithm
    Params:
    row (int): current row
    num (int): size of board
    col (set): set of columns
    pos_diag (set): set of positive diagonals
    neg_diag (set): set of negative diagonals
    """
    global board
    if row == num:
        print(solutions())
        return

    for c in range(num):
        if c in col or row + c in pos_diag or row - c in neg_diag:
            continue

        col.add(c)
        pos_diag.add(row + c)
        neg_diag.add(row - c)

        board[row][c] = 1

        backtrack(row + 1, num, col, pos_diag, neg_diag)

        col.remove(c)
        pos_diag.remove(row + c)
        neg_diag.remove(row - c)

        board[row][c] = 0


def n_queens(num):
    """
    Solves nqueens problem
    Param:
    num (int): size of board
    """
    global board, positions
    col = set()
    pos_diag = set()
    neg_diag = set()

    board = [[0 for i in range(num)] for i in range(num)]
    positions = [[c + r for c in range(2)] for r in range(num)]

    backtrack(0, num, col, pos_diag, neg_diag)


if(len(sys.argv) != 2):
    print("Usage: nqueens N")
    sys.exit(1)

num = sys.argv[1]
try:
    num = int(num)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if(num < 4):
    print("N must be at least 4")
    sys.exit(1)

n_queens(num)

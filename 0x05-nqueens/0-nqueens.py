#!/usr/bin/python3
"""
Solves the N-queens problem.
Finds all possible arrangements of N
non-conflicting queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented as [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen is placed on the chessboard.
"""
import sys


def create_board(n):
    """Create an `n`x`n` chessboard initialized with spaces."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return board


def deep_copy_board(board):
    """Return a deep copy of the chessboard."""
    if isinstance(board, list):
        return list(map(deep_copy_board, board))
    return board


def extract_solution(board):
    """Extract the solution from the chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_conflicts(board, row, col):
    """Mark conflicts on the chessboard.
    All positions where queens can no longer
    be placed without attacking each other are marked.
    Args:
        board (list): The current chessboard state.
        row (int): The row where a queen was placed.
        col (int): The column where a queen was placed.
    """
    # Mark all positions to the right
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all positions to the left
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all positions below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all positions above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all positions diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all positions diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # Mark all positions diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all positions diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_nqueens(board, row, queens, solutions):
    """Recursively solve the N-queens problem.
    Args:
        board (list): The current chessboard state.
        row (int): The current row being processed.
        queens (int): The current count of placed queens.
        solutions (list): A list of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(extract_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = deep_copy_board(board)
            temp_board[row][c] = "Q"
            mark_conflicts(temp_board, row, c)
            solutions = solve_nqueens(temp_board, row + 1,
                                      queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(int(sys.argv[1]))
    solutions = solve_nqueens(board, 0, 0, [])
    for sol in solutions:
        print(sol)

#!/usr/bin/env python3


def validate_file(file):
    lines = file.read().split("\n")
    assert len(lines) == 9, f"Board should have 9 lines, has {len(lines)}"
    for i, line in enumerate(lines):
        assert (
            len(line.split(" ")) == 9
        ), f"Line {i + 1} should have 9 characters, has {len(line.split(' '))}"
        assert (
            len(line) == 17
        ), f"Make sure you have 9 space-seperated numbers. Currently, line {i + 1} has {len(line)} total characters, and should have 17."
    return lines


def read_file(filename):
    with open(filename, "r") as f:
        lines = validate_file(f)
    return [line.split(" ") for _, line in enumerate(lines)]


def print_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()


def board_to_file(board):
    with open("puzzle.txt", "w") as f:
        for i in board:
            for j in i:
                f.write(f"{j} ")
            f.write("\n")


def has_all_digits(lst):
    return "".join(sorted(lst)) != "123456789"


def is_solved(board):
    for i in range(9):
        for j in range(9):
            if any(
                [
                    has_all_digits(get_from_row(board, i)),
                    has_all_digits(get_from_column(board, j)),
                    has_all_digits(get_from_square(board, get_square_index(i, j))),
                ]
            ):
                return False
    return True


def check_board(board, row_idx, col_idx):
    """Given a board, row index, and column index, return a list of possible digits"""
    return find_remaining(
        combine_lists(
            get_from_row(board, row_idx),
            get_from_column(board, col_idx),
            get_from_square(board, get_square_index(row_idx, col_idx)),
        )
    )


def get_from_row(board, row_idx):
    """Get a list of numbers from a given row in the board."""
    row = [i for i in board[row_idx] if i != "0"]
    assert len(row) <= 9
    return row


def get_from_column(board, column_idx):
    """Get a list of numbers from a given column in the board."""
    column = [row[column_idx] for row in board if row[column_idx] != "0"]
    assert len(column) <= 9
    return column


def get_square_index(row_idx, col_idx):
    """Convert a 9x9 index to a 1x9 index (3x3)"""
    assert row_idx < 9
    assert col_idx < 9
    return row_idx // 3 * 3 + col_idx // 3


def get_from_square(board, square_idx):
    """
    Get a list of numbers from a given square in the board. See indices below:

    0  1  2\n
    3  4  5\n
    6  7  8
    """
    assert square_idx < 9, f"index should be less than 9, is {square_idx}"
    assert len(board) == 9, f"board should have 9 rows, has {len(board)}"
    for i in range(9):
        assert (
            len(board[i]) == 9
        ), f"length of row {i} should be 9, is {len(board[i])}, {board[i]}"
    row = square_idx // 3
    column = square_idx % 3
    output = []
    for i in range(3):
        for j in range(3):
            item = board[row * 3 + i][column * 3 + j]
            if item != "0":
                output.append(item)
    return output


def remove_zeros(iter):
    """Removes zeros from a list"""
    for _ in range(iter.count("0")):
        iter.remove("0")
    return iter


def combine_lists(a, b, c):
    """Combines lists of numbers"""
    chars = remove_zeros([*a, *b, *c])
    for i in chars.copy():
        if chars.count(i) > 1:
            chars.remove(i)
    assert (
        len(chars) <= 9
    ), f"There are {len(chars)}, but there should be 9 or fewer: {chars}"
    assert len(chars) == len(
        set(chars)
    ), f"Repeating digits in row, column, or square not allowed: {max(set(chars), key = chars.count)}, {chars}"
    return chars


def find_remaining(numbers):
    remaining = list("123456789")
    for i in numbers:
        remaining.remove(i)
    return remaining


def main():
    puzzle = read_file("puzzle.txt")
    while not is_solved(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != "0":
                    continue
                possible_chars = check_board(puzzle, i, j)
                if len(possible_chars) == 1:
                    puzzle[i][j] = possible_chars[0]
                    print(".")
    print_board(puzzle)


if __name__ == "__main__":
    main()

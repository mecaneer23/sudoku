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


def check_board(board):
    for i in 9:
        for j in 9:
            find_remaining(
                combine_lists(
                    get_from_row(board, i), get_from_column(board, j), get_from_square(board, get_square_index(i, j))
                )
            )


def get_from_row(board, row_idx):
    """Get a list of numbers from a given row in the board."""
    return [i for i in board[row_idx] if i != "0"]


def get_from_column(board, column_idx):
    """Get a list of numbers from a given column in the board."""
    return [row[column_idx] for row in board if row[column_idx] != "0"]


def get_square_index(row_idx, col_idx):
    return row_idx // 3 * 3 + col_idx // 3


def get_from_square(board, square_idx):
    """
    Get a list of numbers from a given square in the board. See indices below:

    0  1  2\n
    3  4  5\n
    6  7  8
    """
    row = square_idx // 3
    column = square_idx % 3
    output = []
    for i in range(3):
        for j in range(3):
            item = board[row*3 + i][column*3 + j]
            if item != "0":
                output.append(item)
    return output


def combine_lists(a, b, c):
    """Combines lists of numbers"""
    chars = [*a, *b, *c]
    assert len(chars) <= 9
    assert len(chars) == len(
        set(chars)
    ), "Repeating digits in row, column, or square not allowed"
    return chars


def find_remaining(numbers):
    remaining = list("123456789")
    for i in numbers:
        remaining.remove(i)
    return remaining


# iterate through board to solve
def main():
    puzzle = read_file("puzzle.txt")
    print(get_from_square(puzzle, 5))


if __name__ == "__main__":
    main()

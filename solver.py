#!/usr/bin/env python3

def validate_file(file):
    lines = file.read().split("\n")
    assert len(lines) == 9, f"Board should have 9 lines, has {len(lines)}"
    for i, line in enumerate(lines):
        assert len(line.split(" ")) == 9, f"Line {i + 1} should have 9 characters, has {len(line.split(' '))}"
        assert len(line) == 17, f"Make sure you have 9 space-seperated numbers. Currently, line {i + 1} has {len(line)} total characters, and should have 17."
    return lines


def read_file(filename):
    with open(filename, 'r') as f:
        lines = validate_file(f)
    return [line.split(" ") for _, line in enumerate(lines)]


def print_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

# iterate through board to solve
# write to string
# write to file
def main():
    puzzle = read_file("puzzle.txt")


if __name__ == '__main__':
    main()

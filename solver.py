#!/usr/bin/env python3

def validate_file(file):
    lines = file.read().split("\n")
    assert len(lines) == 9
    for line in lines:
        assert len(line.split(" ")) == 9
        assert len(line) == 17, len(line)
    return lines


def read_file(filename):
    with open(filename, 'r') as f:
        lines = validate_file(f)
        output = [line.split(" ") for _, line in enumerate(lines)]
        # parse text file to lists

# iterate through board to solve
# write to string
# write to file
def main():
    puzzle = read_file("puzzle.txt")


if __name__ == '__main__':
    main()

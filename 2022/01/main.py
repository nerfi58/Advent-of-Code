import os

DIR = os.path.dirname(os.path.realpath(__file__))


class Part1:
    def __init__(self, file):
        with open(file) as f:
            pass


def main():
    part1 = Part1(os.path.join(DIR, 'input.txt'))


if __name__ == '__main__':
    main()

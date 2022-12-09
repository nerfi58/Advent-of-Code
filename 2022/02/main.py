import os

DIR = os.path.dirname(os.path.realpath(__file__))
POINTS = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
OPTIONS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2,
}


class Elf:
    def __init__(self, input_path):
        with open(input_path) as f:
            self.__lines = [line.strip().split(' ') for line in f]

    @property
    def part1(self):
        sum = 0
        for line in self.__lines:
            if OPTIONS[line[0]] == OPTIONS[line[1]]:
                points = 3

            elif (OPTIONS[line[0]] + 1) % 3 == OPTIONS[line[1]] % 3:
                points = 6

            else:
                points = 0

            sum += points + POINTS[line[1]]

        return sum

    @property
    def part2(self):
        sum = 0
        for line in self.__lines:
            if line[1] == 'X':
                points = 0
                choice = (OPTIONS[line[0]] + 2) % 3

            elif line[1] == 'Y':
                points = 3
                choice = OPTIONS[line[0]]

            else:
                points = 6
                choice = (OPTIONS[line[0]] + 1) % 3

            sum += points + POINTS[list(OPTIONS.keys())[-3:][choice]]

        return sum


def main():
    elf = Elf(os.path.join(DIR, 'input.txt'))
    print(f'Part 1 solution: {elf.part1}')
    print(f'Part 2 solution: {elf.part2}')


if __name__ == '__main__':
    main()

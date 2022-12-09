import os

DIR = os.path.dirname(os.path.realpath(__file__))


class Elf:
    def __init__(self, file):
        self.__elves = {0: 0}
        with open(file) as f:
            elf = 0
            for line in f:
                if line.strip() == '':
                    elf += 1
                    self.__elves[elf] = 0
                else:
                    self.__elves[elf] += int(line.strip())

    @property
    def part1(self):
        return sorted(self.__elves.values())[-1]

    @property
    def part2(self):
        return sum(sorted(self.__elves.values())[-3:])


def main():
    elf = Elf(os.path.join(DIR, 'input.txt'))
    print(f"Part 1 solution: {elf.part1}")
    print(f"Part 2 solution: {elf.part2}")


if __name__ == '__main__':
    main()

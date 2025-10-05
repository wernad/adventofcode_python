from dataclasses import dataclass
from common.day import Day
from collections import Counter


@dataclass
class DoubleList:
    left: list
    right: list


class Day1(Day):
    DAY = 1
    YEAR = 2024

    def __init__(self, file_path: str) -> None:
        """Creates Day object for day 2024-12-01.

        Args:
            file_path: path to input file.
        """
        super().__init__(file_path=file_path)

    def process_input(self, raw: str) -> DoubleList:
        """Parses text file into DoubleList.

        Expects text file with 1 tuple per line.
        Creates 2 lists containing elements from one side of the tuples.

        Args:
            raw: raw text file.

        Returns:
            DoubleList structure.
        """

        lines = raw.splitlines()
        left = []
        right = []

        for line in lines:
            left_item, right_item = line.split("   ")
            left.append(int(left_item))
            right.append(int(right_item))

        return DoubleList(left=left, right=right)

    def solve_part_1(self) -> None:
        """Sums distances between elements of sorted left and right lists."""
        data: DoubleList = self.input_data.processed

        data.left.sort()
        data.right.sort()

        _sum = 0
        for a, b in zip(data.left, data.right):
            _sum += abs(a - b)

        self.part_1 = _sum

    def solve_part_2(self) -> None:
        """Finds score based on occurences of left list items in right list."""
        data: DoubleList = self.input_data.processed

        left_set = set(data.left)
        right_counter = Counter(data.right)

        self.part_2 = sum([item * right_counter[item] for item in left_set])

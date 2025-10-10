import re
from common.day import Day


class Day3(Day):
    DAY = 3
    YEAR = 2024

    def __init__(self, file_path: str) -> None:
        """Creates Day object for day 2024-12-03.

        Args:
            file_path: path to input file.
        """
        super().__init__(file_path=file_path)

    def process_input(self, raw: str) -> str:
        """Returns original file content as no processing is needed.

        Args:
            raw: raw text file.

        Returns:
            Original file content in string variable.
        """

        return raw

    def solve_part_1(self) -> None:
        """Finds all occurences of valid mul commands and calculates sum of it's results."""

        rgx = r"mul\((\d{1,3},\d{1,3})\)"
        found = re.findall(rgx, self.input_data.processed)

        total = 0

        for group in found:
            left, right = group.split(",")
            total += int(left) * int(right)

        self.part_1 = total

    def solve_part_2(self) -> None:
        """Finds all occurences of valid mul commands.

        Ignores mul commands in 'dont' scope and calculates sum of it's results.
        """

        rgx = r"mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don't\(\))"
        found = re.findall(rgx, self.input_data.processed)

        total = 0

        do = True
        for group in found:
            if do:
                try:
                    left, right = group[0].split(",")
                    total += int(left) * int(right)
                except ValueError:
                    if group[2] != "":
                        do = False
            else:
                if group[1] != "":
                    do = True

        self.part_2 = total

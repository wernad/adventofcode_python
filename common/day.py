from typing import Any
from common.structures import DayInput


class Day:
    YEAR: int
    DAY: int
    input_data: DayInput
    part_1: int = None
    part_2: int = None

    def __init__(self, file_path: str) -> None:
        """Creates a new Day object with loaded puzzle input.

        Args:
            file_path: path to the input file. Expects txt file.
        """
        with open(file_path) as f:
            raw = f.read()

        processed = self.process_input(raw)

        self.input_data = DayInput(raw=raw, processed=processed)

    def get_result_string(self) -> str:
        """Creates and returns a Result object with results to both parts of the day.

        Returns:
            Result object.
        """

        return (
            f"Day {self.YEAR}-{self.DAY}:\nPart 1: {self.part_1}\nPart 2: {self.part_2}"
        )

    def solve_part_1(self) -> None:
        """Solves a given part of the task and stores it."""

    def solve_part_2(self) -> None:
        """Solves a given part of the task and stores it."""

    def process_input(self, raw: str) -> Any:
        """Processes raw input file into format specific to a task and returns it. Implement in subclass."""

    def solve(self) -> None:
        """Solves both parts of the day's task."""
        self.solve_part_1()
        self.solve_part_2()

from enum import Enum
from common.day import Day
from operator import gt, lt


class ReportType(Enum):
    INC = 0
    DEC = 1


class Day2(Day):
    DAY = 2
    YEAR = 2024

    def __init__(self, file_path: str) -> None:
        """Creates Day object for day 2024-12-02.

        Args:
            file_path: path to input file.
        """
        super().__init__(file_path=file_path)

    def process_input(self, raw: str) -> list[int]:
        """Parses text file into list of lists with integers.

        Expects lines of numbers.

        Args:
            raw: raw text file.

        Returns:
            list
        """

        lines = raw.splitlines()
        reports = []

        for line in lines:
            reports.append([int(x) for x in line.split(" ")])

        return reports

    @staticmethod
    def validate_report(
        report: list[int], inc: ReportType, min_diff: int = 1, max_diff: int = 3
    ) -> list[bool]:
        """Checks if values are incrementing (or decrementing) in given range or not.

        Args:
            inc: if check as incrementing or decrementing.
            report: list of values to check.
            min_dif: minimum difference between values.
            max_dif: maximum difference between values.
        Returns:
            List of booleans indicating valid values.
        """

        operator = gt
        if inc == ReportType.INC:
            operator = lt

        return [
            operator(value_1, value_2)
            and min_diff <= abs(value_1 - value_2) <= max_diff
            for value_1, value_2 in zip(report[:-1], report[1:])
        ]

    @staticmethod
    def attempt_fix(report: list[int], error_idx: int, inc: ReportType) -> bool:
        """Revalidates given report while removing a single value at a time.

        Attempts to fix are done by popping one of the values that caused an error.

        Args:
            report: list of values to validate.
            error_idx: which index contains faulty value.
            inc: validate as increasing or decreasing report.
        Returns:
            Bool indicating success or failure to fix report."""

        for idx in range(error_idx, error_idx + 2):
            report_copy = report.copy()

            report_copy.pop(idx)
            revalidated = Day2.validate_report(inc=inc, report=report_copy)

            if revalidated.count(False) == 0:
                return True

        return False

    def solve_part_1(self) -> None:
        """Finds number of valid reports in list of lists."""

        count = 0
        for report in self.input_data.processed:
            if all(Day2.validate_report(inc=ReportType.INC, report=report)):
                count += 1
            elif all(Day2.validate_report(inc=ReportType.DEC, report=report)):
                count += 1
        self.part_1 = count

    def solve_part_2(self) -> None:
        """Find fixable reports and return their count."""
        valid_count = 0
        for report in self.input_data.processed:
            # Increasing.
            validated = Day2.validate_report(inc=ReportType.INC, report=report)
            error_count = validated.count(False)

            if error_count == 0:
                valid_count += 1
                continue
            else:
                idx = validated.index(False)
                result = Day2.attempt_fix(
                    report=report, error_idx=idx, inc=ReportType.INC
                )
                if result:
                    valid_count += 1
                    continue

            # Decreasing.
            validated = Day2.validate_report(inc=True, report=report)
            error_count = validated.count(False)

            if error_count == 0:
                valid_count += 1
            else:
                idx = validated.index(False)
                valid_count += Day2.attempt_fix(
                    report=report, error_idx=idx, inc=ReportType.DEC
                )
        self.part_2 = valid_count

from common.day import Day
from solutions import YEARS


class Advent:
    years: dict[int, dict[int, callable]]

    def __init__(self) -> None:
        """Init method for a year object."""
        self.years = {}
        for year, days in YEARS.items():
            self.years[year] = {}
            for day, cls in days.items():
                self.years[year][day] = cls

    def get_solution(self, year: int, day: int, file_path: str | None) -> str:
        """Retrieves a result for given day and year in a string format.

        Args:
            year: year to find.
            day: day to find.
        Returns:
            Returns a string containg results for both parts.
        """

        try:
            cls = self.years[year][day]
        except KeyError:
            print(f"Year {year} Day {day} not found.")
            
        day_obj: Day = cls(file_path=file_path)
        day_obj.solve()

        result = day_obj.get_result_string()
        return result

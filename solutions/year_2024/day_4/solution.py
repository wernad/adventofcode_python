from dataclasses import dataclass, astuple
from enum import Enum
from typing import Callable

from common.day import Day



type Grid = dict[Point, str]
type DirectionFunc = Callable[[int, int, Grid], int]

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(x=self.x + other.x, y=self.y + other.y)
    
class Direction(Enum):
    LEFT = Point(x=-1, y=0)
    TOP_LEFT = Point(x=-1, y=-1)
    TOP = Point(x=0, y=-1)
    TOP_RIGHT = Point(x=1, y=-1)
    RIGHT = Point(x=1, y=0)
    BOTTOM_RIGHT = Point(x=1, y=1)
    BOTTOM = Point(x=0,y= 1)
    BOTTOM_LEFT = Point(x=-1, y=1)



class Day4(Day):
    DAY = 4
    YEAR = 2024

    def __init__(self, file_path: str) -> None:
        """Creates Day object for day 2024-12-04.

        Args:
            file_path: path to input file.
        """
        super().__init__(file_path=file_path)

    def process_input(self, raw: str) -> Grid:
        """Processes raw string file into 2D grid via nested lists.

        Args:
            raw: raw text file.

        Returns:
            list of lists representing 2D grid of strings.
        """

        
        lines = raw.strip().split('\n')
        grid = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                p = Point(x=x, y=y)
                grid[p] = char
        return grid

    def count_omni_xmas(self, p: Point, grid: Grid) -> int:
        """Checks if word 'XMAS' is present in 8 directions from given (x, y) center.
        
        Args:
            p: Point object with x and y coordinates.
            grid: grid object to traverse.
        Result:
            Count of occurences as integer.
        """

        directions = [direction.value for direction in Direction]

        letters = ['M', 'A', 'S']

        count = 0 
        for dir in directions:
            if p.x + 3 * dir.x < 0 or p.y + 3 * dir.y < 0:
                continue
            next_p = p + dir
            
            try:
                for letter in letters:
                    if grid[next_p] != letter:
                        break
                    next_p += dir
                else:
                    count += 1
            except KeyError:
                continue
        return count
    
    @staticmethod
    def get_cross_letters(p: Point, grid: Grid, directions: list[Direction]) -> str:
        """Calculates new points from given origin and changes to be applied.
        
        Args:
            p: Point object with x and y coordinates.
            directions: list of changes to be applied to origin.
        Returns:
            string with extracted letters.
        """
        
        result = ""

        for dir in directions:
            try:
                new_p = p + dir.value
                letter = grid[new_p]
                result += letter
            except KeyError:
                continue
            

        return result
    
    def count_cross_mas(self, p: Point, grid: Grid) -> int:
        """Checks if word 'MAS' is centered in cross pattern around given (x, y) point.
        
         Args:
            p: Point object with x and y coordinates.
            grid: grid object to check.
        Result:
            Count of occurences as integer.
        """
        strings = ["MS", "SM"]

        first_half = Day4.get_cross_letters(p, grid, [Direction.TOP_LEFT, Direction.BOTTOM_RIGHT])
        second_half = Day4.get_cross_letters(p, grid, [Direction.TOP_RIGHT, Direction.BOTTOM_LEFT])
        
        if first_half in strings and second_half in strings:
            return 1
        return 0

    def count_occurences(self, count_func: DirectionFunc, center_letter: str) -> int:
        """Gets number of occurences of words in given ruleset if current letter is equal to 'center_letter'.

        Args:
            ruleset: list of Rules to check.
            center_letter: which letter to start with.
        Returns:
            count as integer.
        """

        grid = self.input_data.processed
        total = 0
        for point, letter in grid.items():
            if letter == center_letter:
                total += count_func(point, grid)
        return total

    def solve_part_1(self) -> None:
        """Counts all occurences of word 'XMAS' in 8 directions."""

        total = self.count_occurences(self.count_omni_xmas, "X")
        self.part_1 = total

    def solve_part_2(self) -> None:
        """Counts all occurences of a 'MAS' word in X-like shape with A being in center."""

        total = self.count_occurences(self.count_cross_mas, "A")
 
        self.part_2 = total
    
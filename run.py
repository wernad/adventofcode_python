import argparse as ap

from advent import Advent

parser = ap.ArgumentParser(
    prog="Advent of Code 2023 Python",
    description="Shows solutions for daily tasks in AoC 2023 in Python",
)

parser.add_argument(
    "-f", "--file", help="Specifies puzzle input file. Expects .txt format."
)
parser.add_argument("-d", "--day", default=1, help="Day of the advent.")
parser.add_argument("-y", "--year", default=2024, help="Year of the advent.")

parser.add_argument("-a", "--api", default=False, help="Start an API server.")

args = parser.parse_args()


if __name__ == "__main__":
    if args.api:  # TODO
        pass
    else:
        if not args.file:
            print("Missing file path to input file.")
        else:
            advent = Advent()
            year = int(args.year)
            day = int(args.day)
            result = advent.get_solution(year=year, day=day, file_path=args.file)
            print(result)

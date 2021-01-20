"""replace tabs with spaces in files!"""

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from typing import Tuple, Iterable

def parse_args() -> Tuple[int, Tuple[str, ...]]:
    parser = ArgumentParser(
        description = __doc__,
        formatter_class = ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--tabstop",
        type = int,
        default = 4,
        help = "number of spaces to replace each tab character with"
    )
    parser.add_argument(
        "filename",
        type = str,
        nargs = "+",
        help = "name of file to retab"
    )
    args = parser.parse_args()
    return args.tabstop, args.filename

def main(tabstop: int, filenames: Iterable[str]) -> None:
    for filename in filenames:
        print(f'retabbing "{filename}"...', end = " ")
        try:
            with open(filename, "r+") as file:
                text = file.read()
                file.seek(0)
                file.write(text.replace("\t", " " * tabstop))
            print("done.")
        except FileNotFoundError:
            print("file not found!")

if __name__ == "__main__":
    main(*parse_args())

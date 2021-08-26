import ffmpeg
from argparse import ArgumentParser
from pathlib import Path
from typing import Iterable

def parse_args() -> Path:
    parser = ArgumentParser()
    parser.add_argument("rootpath", nargs = "?", type = Path, default = Path())
    return parser.parse_args().rootpath

def main(paths: Iterable[Path]) -> None:
    paths = tuple(paths)
    print("crunchcating...")
    for p in paths:
        print(f"- {p}")
    ffmpeg.concat(*(ffmpeg.input(p) for p in paths)).output("out.webm").run()

if __name__ == "__main__":
    main(parse_args().rglob("*"))

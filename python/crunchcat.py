import ffmpeg
from argparse import ArgumentParser
from pathlib import Path
from typing import Iterable

def parse_args() -> Path:
    parser = ArgumentParser()
    parser.add_argument("rootpath", nargs = "?", default = Path(), type = Path)
    parser.add_argument("-o", "--output", type = Path, required = True)
    args = parser.parse_args()
    return args.rootpath.rglob("*"), args.output

def main(paths: Iterable[Path], output: Path) -> None:
    ffmpeg.concat(
        *(ffmpeg.input(p) for p in paths)
    ).output(
        str(output) + ".webm"
    ).run()

if __name__ == "__main__":
    main(*parse_args())

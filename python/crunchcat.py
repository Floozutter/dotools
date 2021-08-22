import ffmpeg
from argparse import ArgumentParser
from pathlib import Path

def parse_args() -> Path:
    parser = ArgumentParser()
    parser.add_argument("rootpath", nargs = "?", type = Path, default = Path())
    return parser.parse_args().rootpath

def main(rootpath: Path) -> None:
    pass

if __name__ == "__main__":
    main(parse_args())

import ffmpeg
from argparse import ArgumentParser
from pathlib import Path

def parse_args() -> Path:
    parser = ArgumentParser()
    parser.add_argument("rootpath", nargs = "?", type = Path, default = Path())
    return parser.parse_args().rootpath

if __name__ == "__main__":
    parse_args()

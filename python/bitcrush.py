"""
bitcrush WAVE files!
"""


from argparse import ArgumentParser
from pathlib import Path

def parse_args() -> tuple[Path, Path]:
    parser = ArgumentParser(description = __doc__)
    return Path(), Path()

def main(iwavepath: Path, owavePath: Path) -> None:
    pass

if __name__ == "__main__":
    main(*parse_args())

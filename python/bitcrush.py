"""
bitcrush WAVE files!
"""

import wave
from argparse import ArgumentParser
from pathlib import Path

def parse_args() -> tuple[Path, Path]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("iwavepath", type = Path)
    parser.add_argument("owavepath", type = Path)
    args = parser.parse_args()
    return args.iwavepath, args.owavepath

def main(iwavepath: Path, owavepath: Path) -> None:
    with wave.open(str(iwavepath, "r")) as iwave:
        pre = ()
    post = ()
    with wave.open(str(owavepath.with_suffix(".wav")), "w") as owave:
        pass

if __name__ == "__main__":
    main(*parse_args())

"""
synthesize sine waves into a chord!
"""

import wave
import math
from pathlib import Path
from argparse import ArgumentParser
from struct import pack
from typing import Iterable

WIDTH = 2
MAX_VALUE = 2**(8*WIDTH - 1) - 1
RATE = 44100
A4 = 440

def parse_args() -> tuple[tuple[float, ...], Path]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("pitches", nargs = "+", type = str)
    parser.add_argument("-o", "--outpath", type = str, required = True)
    args = parser.parse_args()
    return tuple(args.pitches), args.outpath

def main(pitches: Iterable[float], out: Path) -> None:
    samples = ()
    with wave.open(str(out), "w") as owave:
        owave.setnchannels(1)
        owave.setsampwidth(WIDTH)
        owave.setframerate(RATE)
        for sample in samples:
            value = int(MAX_VALUE * sample)
            owave.writeframes(pack("<h", value))

if __name__ == "__main__":
    main(*parse_args())

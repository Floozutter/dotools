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

def parse_args() -> tuple[tuple[float, ...], float, float, Path]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("pitches", nargs = "+", type = float)
    parser.add_argument("-d", "--duration", type = float, default = 1)
    parser.add_argument("-v", "--volume", type = float, default = 0.5)
    parser.add_argument("-o", "--outpath", type = str, required = True)
    args = parser.parse_args()
    if args.duration < 0:
        parser.error("argument -d/--duration: must be nonnegative")
    elif args.volume < 0 or args.volume > 1:
        parser.error("argument -v/--volume: must be in [0, 1]")
    else:
        return tuple(args.pitches), args.duration, args.volume, args.outpath

def main(pitches: Iterable[float], duration: float, volume: float, out: Path) -> None:
    voices = tuple(
        tuple(
            volume * math.sin(2*math.pi * pitch * i / RATE)
            for i in range(int(RATE * duration))
        )
        for pitch in pitches
    )
    samples = tuple(map(sum, zip(*voices)))
    with wave.open(str(out), "w") as owave:
        owave.setnchannels(1)
        owave.setsampwidth(WIDTH)
        owave.setframerate(RATE)
        for sample in samples:
            value = max(min(int(MAX_VALUE * sample), MAX_VALUE), -MAX_VALUE)
            owave.writeframes(pack("<h", value))

if __name__ == "__main__":
    main(*parse_args())

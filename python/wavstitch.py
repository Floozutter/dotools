"""
stitch multiple wav files together into one!
"""

from wave import open as open_wave, _wave_params as wave_params
from argparse import ArgumentParser
from sys import exit
from typing import Iterable

def parse_args() -> tuple[tuple[str, ...], str]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("infile", nargs = "+", type = str, help = "input wav file to stitch")
    parser.add_argument("-o", "--outfile", type = str, required = True, help = "output wav file")
    args = parser.parse_args()
    return tuple(args.infiles), outfile

def main(infiles: Iterable[str], outfile: str) -> int:
    # https://stackoverflow.com/a/2900266
    data: list[tuple[wave.wave_params, bytes]] = []
    for infile in infiles:
        with open_wave(infile, "rb") as iwave:
            data.append((iwave.getparams(), iwave.readframes(iwave.getnframes())))
    with open_wave(outfile, "wb") as owave:
        owave.setparams(data[0][0])
        for _, frames in data:
            owave.writeframes(frames)
    print("done.")
    return 0

if __name__ == "__main__":
    exit(main(*parse_args()))

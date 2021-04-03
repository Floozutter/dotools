"""
stitch multiple wav files together into one!
"""

import wave
from argparse import ArgumentParser
from sys import exit
from typing import Iterable

def parse_args() -> tuple[tuple[str, ...], str]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("infile", nargs = "+", type = str, help = "input wav file to stitch")
    parser.add_argument("-o", "--outfile", type = str, required = True, help = "output wav file")
    args = parser.parse_args()
    return tuple(args.infile), args.outfile

def main(infiles: Iterable[str], outfile: str) -> int:
    # https://stackoverflow.com/a/2900266
    data: list[tuple[wave._wave_params, bytes]] = []
    for infile in infiles:
        print(f"reading from `{infile}`...", end = " ")
        try:
            with wave.open(infile, "rb") as iwave:
                data.append((iwave.getparams(), iwave.readframes(iwave.getnframes())))
        except OSError as e:
            print(f"os error: `{e}`!")
            return 1
        except wave.Error as e:
            print(f"wav error: `{e}`!")
            return 1
        else:
            print("done.")
    print(f"writing to `{outfile}`...", end = " ")
    try:
        with wave.open(outfile, "wb") as owave:
            owave.setparams(data[0][0])
            for _, frames in data:
                owave.writeframes(frames)
    except OSError as e:
        print(f"os error: `{e}`!")
        return 1
    except wave.Error as e:
        print(f"wav error: `{e}`!")
        return 1
    else:
        print("done.")
    return 0

if __name__ == "__main__":
    exit(main(*parse_args()))

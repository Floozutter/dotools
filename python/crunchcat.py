import ffmpeg
from argparse import ArgumentParser
from pathlib import Path
from typing import TypeVar, Iterable, Iterator

T = TypeVar("T")
def interleave(*iterables: Iterable[T]) -> Iterator[T]:
    return (value for group in zip(*iterables) for value in group)

def crunch_video(stream):
    return stream.video

def crunch_audio(stream):
    return stream.audio

def parse_args() -> Path:
    parser = ArgumentParser()
    parser.add_argument("rootpath", nargs = "?", default = Path(), type = Path)
    parser.add_argument("-o", "--output", type = Path, required = True)
    args = parser.parse_args()
    return args.rootpath.rglob("*"), args.output

def main(paths: Iterable[Path], output: Path) -> None:
    inps = tuple(ffmpeg.input(p) for p in paths)
    vids = tuple(map(crunch_video, inps))
    auds = tuple(map(crunch_audio, inps))
    ffmpeg.concat(
        *interleave(vids, auds),
        v = 1, a = 1
    ).output(
        str(output) + ".webm"
    ).run()

if __name__ == "__main__":
    main(*parse_args())

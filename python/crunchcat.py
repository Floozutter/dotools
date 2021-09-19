import ffmpeg
from argparse import ArgumentParser
from pathlib import Path
from typing import TypeVar, Iterable, Iterator

T = TypeVar("T")
def interleave(*iterables: Iterable[T]) -> Iterator[T]:
    return (value for group in zip(*iterables) for value in group)

def crunch_video(stream):
    return (
        stream.video
            .filter("scale", 64, 32)
            .filter("fps", fps = 4)
    )

def crunch_audio(stream):
    return stream.audio

def parse_args() -> tuple[tuple[Path, ...], Path]:
    parser = ArgumentParser()
    parser.add_argument("rootpath", nargs = "?", default = Path(), type = Path)
    parser.add_argument("-o", "--output", type = Path, required = True)
    args = parser.parse_args()
    return tuple(args.rootpath.rglob("*")), args.output

def main(paths: Iterable[Path], output: Path) -> None:
    inps = tuple(map(ffmpeg.input, paths))
    vids = tuple(map(crunch_video, inps))
    auds = tuple(map(crunch_audio, inps))
    command = ffmpeg.concat(
        *interleave(vids, auds),
        v = 1, a = 1
    ).output(
        str(output) + ".webm",
        format = "webm",
        vcodec = "libaom-av1",
        crf = 63,
        video_bitrate = 1000,
        acodec = "libopus",
        audio_bitrate = 4000,
        cutoff = 4000
    )
    # to-do: 2-pass
    command.run()

if __name__ == "__main__":
    main(*parse_args())

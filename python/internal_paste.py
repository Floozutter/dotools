"""
pastes an image region elsewhere!
made as a demo for Rachel
"""

from argparse import ArgumentParser
from PIL import Image

def parse_args() -> tuple[str, str, int, int, int, int, int]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("ifilename", type = str, help = "input image")
    parser.add_argument("ofilename", type = str, help = "output image")
    parser.add_argument("sx", type = int, help = "x of source top-left")
    parser.add_argument("sy", type = int, help = "y of source top-left")
    parser.add_argument("tx", type = int, help = "x of dest top-left")
    parser.add_argument("ty", type = int, help = "y of dest top-left")
    parser.add_argument("width", type = int, help = "width of region")
    parser.add_argument("height", type = int, help = "height of region")
    args = parser.parse_args()
    return (
        args.ifilename,
        args.ofilename,
        args.sx,
        args.sy,
        args.tx,
        args.ty,
        args.width,
        args.height,
    )

def internal_paste(
    img: Image,
    sx: int, sy: int,
    tx: int, ty: int,
    width: int, height: int
) -> Image:
    ret = img.copy()
    for x in range(width):
        for y in range(height):
            ret.putpixel((tx + x, ty + y), ret.getpixel((sx + x, sy + y)))
    return ret

def main(
    ifilename: str, ofilename: str,
    sx: int, sy: int,
    tx: int, ty: int,
    width: int, height: int
) -> None:
    with Image.open(ifilename) as src:
        internal_paste(src, sx, sy, tx, ty, width, height).save(ofilename)

if __name__ == "__main__":
    main(*parse_args())

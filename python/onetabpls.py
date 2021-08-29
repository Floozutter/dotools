from pyquery import PyQuery
from pathlib import Path
from argparse import ArgumentParser
from typing import NamedTuple

class Tab(NamedTuple):
    url: str
    title: str

def read_page(doc: PyQuery) -> tuple[Tab, ...]:
    anchors = doc("a")
    return tuple(
        Tab(PyQuery(a).attr("href"), a.text)
        for a in anchors
    )

def parse_args() -> Path:
    parser = ArgumentParser()
    parser.add_argument("rootpath", nargs = "?", type = Path, default = Path())
    return parser.parse_args().rootpath

if __name__ == "__main__":
    rootpath = parse_args()
    pagepaths = tuple(rootpath.rglob("*.html"))
    data = tuple(
        tab
        for path in pagepaths
        for tab in read_page(PyQuery(path.read_text()))
    )
    print(f"{len(data)} tabs read into variable `data`.")

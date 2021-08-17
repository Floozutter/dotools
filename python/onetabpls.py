from pyquery import PyQuery
from pathlib import Path
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

if __name__ == "__main__":
    pagepaths = tuple(Path().rglob("*.html"))
    data = tuple(
        tab
        for path in pagepaths
        for tab in read_page(PyQuery(path.read_text()))
    )
    print(f"{len(data)} tabs read.")

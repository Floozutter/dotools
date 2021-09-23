from pathlib import Path

def parse_args() -> tuple[Path, Path]:
    return Path(), Path()

def main(iwavepath: Path, owavePath: Path) -> None:
    pass

if __name__ == "__main__":
    main(*parse_args())

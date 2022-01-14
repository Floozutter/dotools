"""
solver for https://www.powerlanguage.co.uk/wordle/
"""

from argparse import ArgumentParser
from pathlib import Path
from functools import cache
from collections import Counter
from enum import Enum

class Hint(Enum):
    NOWHERE = "0"
    OTHERWHERE = "1"
    THERE = "2"

def choose_guess(words: frozenset[str]) -> str:
    # score guesses by how common their unique letters are (regardless of position)
    total_counter = Counter(c for w in words for c in w)
    t_score = lambda w: sum(total_counter[c] for c in frozenset(w))
    # score guesses by how common each letter is in their respective column
    column_counters: tuple[Counter[str], ...] = tuple(map(Counter, zip(*words)))
    c_score = lambda w: sum(counter[c] for c, counter in zip(w, column_counters))
    # choose the guess that maximizes the sum of both scores
    return max(words, key = lambda w: t_score(w) + c_score(w))

@cache
def deduce_hints(guess: str, solution: str) -> tuple[Hint, ...]:
    hints = [
        Hint.THERE if c == target else Hint.OTHERWHERE if c in solution else Hint.NOWHERE
        for c, target in zip(guess, solution)
    ]
    counter = Counter(solution)
    for i in reversed(range(len(hints))):
        if hints[i] is Hint.OTHERWHERE and sum(
            1 for c, h in zip(guess, hints)
            if c == guess[i] and h in {Hint.THERE, Hint.OTHERWHERE}
        ) > counter[guess[i]]:
            hints[i] = Hint.NOWHERE
    return tuple(hints)

def filter_words(words: frozenset[str], guess: str, hints: tuple[Hint, ...]) -> frozenset[str]:
    return frozenset(w for w in words if deduce_hints(guess, w) == hints)

def prompt_hints(guess: str) -> tuple[Hint, ...] | None:
    while True:
        s = input(f"{guess}?: ").strip().lower()
        if s == "!":
            return None
        elif len(s) == len(guess) and all(c in {e.value for e in Hint} for c in s):
            return tuple(map(Hint, s))

def parse_args() -> tuple[Path, int, str | None]:
    parser = ArgumentParser()
    parser.add_argument("lexicon", type = Path)
    parser.add_argument("--solution", type = str)
    parser.add_argument("--n", type = int, default = 5)
    args = parser.parse_args()
    return args.lexicon, args.n, args.solution

def main(lexicon: Path, n: int, solution: str | None) -> None:
    words = frozenset(w.lower() for w in lexicon.read_text().strip().split() if len(w) == n)
    print(f"parsed {len(words)} size-{n} words.")
    if solution is None:
        print("no solution provided; using manual hint input.")
        print("input hints for each guess as a string consisting of `0`s, `1`s, and `2`s.")
        print("`0` = nowhere, `1` = otherwhere, `2` = there.")
        print("if the guessed word is invalid, input an `!` character.")
    i = 0
    while words:
        guess = choose_guess(words)
        if solution is not None:
            hints = deduce_hints(guess, solution)
            print(f"{i}: {guess} {''.join(h.value for h in hints)}")
        else:
            response = prompt_hints(guess)
            if response is None:
                words -= {guess,}
                continue
            hints = response
        if all(h is Hint.THERE for h in hints):
            break
        words = filter_words(words, guess, hints)
        i += 1

if __name__ == "__main__":
    main(*parse_args())

"""The Internet in One Word.

Design: one word that makes a reader laugh and then nod — the whole
internet, endlessly scrolling bad news at 2 a.m., in a single word.
"Doomscroll" is funny on its own, true of the internet as a whole, and
surprising next to the obvious picks ("chaos", "infinite", "loud").
It lands in one beat, and it is a verb anyone who has done it
recognises instantly — which is everyone.

The program writes the word to /output/entry.txt, the file the sealed
gate reads: UTF-8, 1-30 characters, not only whitespace.
"""

import os

WORD = "Doomscroll"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod("/output/entry.txt", 0o644)
    print(WORD)


if __name__ == "__main__":
    main()

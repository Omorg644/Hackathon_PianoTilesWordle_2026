#Functions for piano tiles

import csv
from pathlib import Path
import random

def load_songs(folder: str = "songs") -> dict:
    """Read every CSV in the folder. Returns {song_name: [notes in order]}."""
    songs = {}
    for path in Path(folder).glob("*.csv"):
        with open(path, newline="") as f:
            rows = sorted(csv.DictReader(f), key=lambda r: int(r["note_id"]))
        songs[path.stem] = [r["note"].strip() for r in rows]
    return songs

def get_snippet(songs: dict, length: int):
    """Pick a random song and a random run of `length` notes from it."""
    name = random.choice([n for n, notes in songs.items() if len(notes) >= length])
    start = random.randint(0, len(songs[name]) - length)
    return name, songs[name][start:start + length]

def checking(guess: list[str], answer) -> list[str]:
    colors = ["gray"] * len(answer)
    remaining = {}

    # First pass: exact matches
    for i in range(len(answer)):
        if guess[i] == answer[i]:
            colors[i] = "green"
        else:
            note = answer[i]
            remaining[note] = remaining.get(note, 0) + 1

    # Second pass: notes in the wrong position
    for i in range(len(guess)):
        if colors[i] == "green":
            continue

        note = guess[i]
        if remaining.get(note, 0) > 0:
            colors[i] = "yellow"
            remaining[note] -= 1

    return colors

def calculate_score(solved, attempts, colors, snippet, max_attempts=6):
    """Points for a finished round. `colors` is the colour list from the last guess."""
    if solved:
        points = 600 + (max_attempts - attempts) * 100
    else:
        points = colors.count("green") * 50 + colors.count("yellow") * 15

    sharps = sum("#" in n for n in snippet)
    multiplier = 1 + 0.1 * (len(set(snippet)) - 1) + 0.1 * sharps
    return round(points * multiplier)
import re
from functions import load_songs, get_snippet, checking, calculate_score

MAX_ATTEMPTS = 6
LENGTH = 5
NOTE_PATTERN = re.compile(r"^[A-G]#?\d$")


def main():
    songs = load_songs()
    song_name, answer = get_snippet(songs, LENGTH)
    print(song_name, answer)          # uncomment to cheat while testing

    locked = [None] * LENGTH            # correct notes found so far
    attempts = 0
    solved = False
    colors = []

    while attempts < MAX_ATTEMPTS and not solved:
        print(f"\nAttempt {attempts + 1}/{MAX_ATTEMPTS}")
        print("Locked:", [note or "_" for note in locked])

        guess = input(f"Enter {LENGTH} notes separated by spaces: ").upper().split()

        # bad input doesn't cost an attempt
        if len(guess) != LENGTH or not all(NOTE_PATTERN.match(n) for n in guess):
            print(f"Enter exactly {LENGTH} notes like C4 or F#5.")
            continue

        # keep correct notes in their spots
        guess = [lock or note for lock, note in zip(locked, guess)]

        colors = checking(guess, answer)
        attempts += 1
        print(guess)
        print(colors)

        for i, colour in enumerate(colors):
            if colour == "green":
                locked[i] = guess[i]

        solved = all(c == "green" for c in colors)

    score = calculate_score(solved, attempts, colors, answer)
    if solved:
        print(f"\nSolved in {attempts}! It was {song_name}.")
    else:
        print(f"\nOut of attempts. The answer was {answer} from {song_name}.")
    print("Score:", score)


if __name__ == "__main__":
    main()
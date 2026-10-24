# Need Answers

answer = ["C4", "D4", "E4", "G4", "E4"]

def checking(guess: list[str]) -> list[str]:
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


def main():
    guess = input("Enter 5 notes separated by spaces: ").upper().split()

    if len(guess) != len(answer):
        print("You must enter exactly 5 notes!")
        return

    colors = checking(guess)
    print(colors)

main()

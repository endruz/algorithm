# Puzzle: https://adventofcode.com/2023/day/4
# Input: https://adventofcode.com/2023/day/4/input
# --- Part Two ---

with open("./puzzle_input.txt", "r") as f:
    lines = f.readlines()

scratchcards = {card_id: 1 for card_id in range(1, len(lines) + 1)}
for line in lines:
    splitted = line.strip().split(":")
    card_id = int(splitted[0].lstrip("Card").strip())
    splitted = splitted[-1].strip().split("|")
    winning_numbers = splitted[0].strip().split()
    numbers_we_have = splitted[1].strip().split()
    match_times = 0
    for number in numbers_we_have:
        if number in winning_numbers:
            match_times += 1
    for i in range(1, match_times + 1):
        scratchcards[card_id + i] += scratchcards[card_id]

print(sum(scratchcards.values()))

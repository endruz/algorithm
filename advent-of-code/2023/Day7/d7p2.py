# https://adventofcode.com/2023/day/7
# --- Part Two ---

from collections import Counter

label_list = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
label_map = {v: i for i, v in enumerate(label_list)}

hands_list: list[list[tuple[str, int]]] = [[] for _ in range(7)]


def get_type_index(hands: str) -> int:
    c = Counter(hands)
    jokers = c.pop("J", 0)
    counter = sorted(c.values(), reverse=True)
    if len(counter) == 0 or counter[0] + jokers == 5:
        return 6
    if counter[0] + jokers == 4:
        return 5
    if counter[0] + jokers == 3:
        if counter[1] == 2:
            return 4
        else:
            return 3
    if counter[0] + jokers == 2:
        if counter[1] == 2:
            return 2
        else:
            return 1
    return 0


def cmp(hands1: str, hands2: str) -> int:
    for index in range(len(hands1)):
        v1 = label_map[hands1[index]]
        v2 = label_map[hands2[index]]
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
    return 0


with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        hands, bid = line.strip().split()
        for index, hands_bid_pair in enumerate(hands_list[get_type_index(hands)]):
            if cmp(hands_bid_pair[0], hands) >= 0:
                hands_list[get_type_index(hands)].insert(index, (hands, int(bid)))
                break
        else:
            hands_list[get_type_index(hands)].append((hands, int(bid)))

result = rank = 0
for h in hands_list:
    for hands_bid_pair in h:
        rank += 1
        winnings = hands_bid_pair[1] * rank
        result += winnings

print(result)

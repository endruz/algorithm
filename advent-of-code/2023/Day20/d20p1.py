# Puzzle: https://adventofcode.com/2023/day/20
# Input: https://adventofcode.com/2023/day/20/input
# --- Part One ---

from typing import Dict, Any
from collections import defaultdict
from copy import deepcopy


def get_module_dict():
    return {"input": [], "type": "", "output": []}


modules: Dict[str, Dict[str, Any]] = defaultdict(get_module_dict)
initial_state: Dict[str, Any] = {}

modules["button"]["output"].append("broadcaster")
modules["broadcaster"]["input"].append("button")

with open("./puzzle_input.txt", "r") as f:
    for line in f.readlines():
        splitted = line.strip().split(" -> ")
        if splitted[0] != "broadcaster":
            module_type, module_name = splitted[0][0], splitted[0][1:]
            modules[module_name]["type"] = module_type
        else:
            module_name = "broadcaster"

        modules[module_name]["output"] = splitted[-1].split(", ")
        for module in modules[module_name]["output"]:
            modules[module].setdefault("input", []).append(module_name)

# print(modules)
for module in modules:
    match modules[module]["type"]:
        case "%":
            # False means off, True means on
            initial_state[module] = False
        case "&":
            # False means low pulse, True means high pulse
            initial_state[module] = [False] * len(modules[module]["input"])

# print(initial_state)
current_state = deepcopy(initial_state)
low_pulse_list = []
high_pulse_list = []
button_count = 0
while button_count < 1000:
    # False means low pulse, True means high pulse
    module_list = [("button", False, "broadcaster")]
    button_count += 1
    print(f"button_count: {button_count}".center(100, "="))
    low_pulse_count = high_pulse_count = 0
    while module_list:
        previous_module, pulse, module = module_list.pop(0)
        print(previous_module, pulse, module)

        if pulse:
            high_pulse_count += 1
        else:
            low_pulse_count += 1

        if modules[module]["type"] == "%":
            if not pulse:
                pulse = current_state[module] = not current_state[module]
            else:
                continue
        elif modules[module]["type"] == "&":
            pulse = False if all(current_state[module]) else True

        for m in modules[module]["output"]:
            if modules[m]["type"] == "&":
                i = modules[m]["input"].index(module)
                current_state[m][i] = pulse
            module_list.append((module, pulse, m))
    low_pulse_list.append(low_pulse_count)
    high_pulse_list.append(high_pulse_count)
    if current_state == initial_state:
        break

if button_count < 1000:
    round_count = 1000 // button_count
    remainder = 1000 % button_count

    sum_low_pulse = sum(low_pulse_list) * round_count + sum(low_pulse_list[:remainder])
    sum_high_pulse = sum(high_pulse_list) * round_count + sum(
        high_pulse_list[:remainder]
    )
else:
    sum_low_pulse = sum(low_pulse_list[:1000])
    sum_high_pulse = sum(high_pulse_list[:1000])

print(button_count, sum_low_pulse, sum_high_pulse)

result = sum_low_pulse * sum_high_pulse
print(result)

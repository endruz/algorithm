# Puzzle: https://adventofcode.com/2023/day/17
# Input: https://adventofcode.com/2023/day/17/input
# --- Part One ---

import heapq
from typing import List, NamedTuple

with open("./puzzle_input.txt", "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

height, weight = len(grid), len(grid[0])

class State(NamedTuple):
    heat_loss: int
    row: int
    col: int
    direction: str
    step_length: int


states: List[State] = [
    State(row=0, col=0, direction="EAST", step_length=3, heat_loss=0),
    State(row=0, col=0, direction="SOUTH", step_length=3, heat_loss=0),
]

result = 0

visited = set()

while states:
    # Prioritize the state with the smallest heat_loss value
    state = heapq.heappop(states)

    # states with smaller heat_loss values are processed first,
    # so the final heat_loss must be larger when encountering the same state later.
    # skip it directly.
    if state[1:] in visited:
        continue
    visited.add(state[1:])

    if state.row == height - 1 and state.col == weight - 1:
        result = state.heat_loss
        break

    # maybe it could look prettier?
    if state.direction == "EAST":
        if (row := state.row + 1) < height:
            heapq.heappush(states, State(row=row, col=state.col, direction="SOUTH", step_length=1, heat_loss=state.heat_loss+grid[row][state.col]))
        if (row := state.row - 1) >= 0:
            heapq.heappush(states, State(row=row, col=state.col, direction="NORTH", step_length=1, heat_loss=state.heat_loss+grid[row][state.col]))
        if state.step_length < 3 and (col := state.col + 1) < weight:
            heapq.heappush(states, State(row=state.row, col=col, direction="EAST", step_length=state.step_length + 1, heat_loss=state.heat_loss+grid[state.row][col]))
    elif state.direction == "WEST":
        if (row := state.row + 1) < height:
            heapq.heappush(states, State(row=row, col=state.col, direction="SOUTH", step_length=1, heat_loss=state.heat_loss+grid[row][state.col]))
        if (row := state.row - 1) >= 0:
            heapq.heappush(states, State(row=row, col=state.col, direction="NORTH", step_length=1, heat_loss=state.heat_loss+grid[row][state.col]))
        if state.step_length < 3 and (col := state.col - 1) >= 0:
            heapq.heappush(states, State(row=state.row, col=col, direction="WEST", step_length=state.step_length + 1, heat_loss=state.heat_loss+grid[state.row][col]))
    elif state.direction == "SOUTH":
        if (col := state.col + 1) < weight:
            heapq.heappush(states, State(row=state.row, col=col, direction="EAST", step_length=1, heat_loss=state.heat_loss+grid[state.row][col]))
        if (col := state.col - 1) >= 0:
            heapq.heappush(states, State(row=state.row, col=col, direction="WEST", step_length=1, heat_loss=state.heat_loss+grid[state.row][col]))
        if state.step_length < 3 and (row := state.row + 1) < height:
            heapq.heappush(states, State(row=row, col=state.col, direction="SOUTH", step_length=state.step_length + 1, heat_loss=state.heat_loss+grid[row][state.col]))
    elif state.direction == "NORTH":
        if (col := state.col + 1) < weight:
            heapq.heappush(states, State(row=state.row, col=col, direction="EAST", step_length=1, heat_loss=state.heat_loss+grid[state.row][col]))
        if (col := state.col - 1) >= 0:
            heapq.heappush(states, State(row=state.row, col=col, direction="WEST", step_length=1, heat_loss=state.heat_loss+grid[state.row][col]))
        if state.step_length < 3 and (row := state.row - 1) >= 0:
            heapq.heappush(states, State(row=row, col=state.col, direction="NORTH", step_length=state.step_length + 1, heat_loss=state.heat_loss+grid[row][state.col]))

print(result)

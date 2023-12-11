# Puzzle: https://adventofcode.com/2023/day/5
# Input: https://adventofcode.com/2023/day/5/input
# --- Part Two ---

source_to_destination_list: list[list] = [[] for _ in range(7)]

(
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location,
) = source_to_destination_list

with open("./puzzle_input.txt", "r") as f:
    seeds = [int(seed) for seed in f.readline().lstrip("seeds: ").split()]
    f.readline()
    for source_to_destination in source_to_destination_list:
        f.readline()  # xxx-to-xxx map:
        while line := f.readline().strip():
            source_to_destination.append([int(num) for num in line.split()])


def get_destination(source_to_destination, source):
    for destination_start, source_start, range_length in source_to_destination:
        if source_start <= source < source_start + range_length:
            return source - source_start + destination_start
    return source


def get_location_from_seed(seed):
    soil = get_destination(seed_to_soil, seed)
    fertilizer = get_destination(soil_to_fertilizer, soil)
    water = get_destination(fertilizer_to_water, fertilizer)
    light = get_destination(water_to_light, water)
    temperature = get_destination(light_to_temperature, light)
    humidity = get_destination(temperature_to_humidity, temperature)
    location = get_destination(humidity_to_location, humidity)
    return location


lowest_location = float("inf")

for index in range(0, len(seeds), 2):
    start_seed = seed = seeds[index]
    length_of_range = seeds[index + 1]
    location = get_location_from_seed(seed)
    if location < lowest_location:
        lowest_location = location
    print(seed, location, lowest_location)
    while seed < start_seed + length_of_range:
        location = get_location_from_seed(seed)
        if location < lowest_location:
            lowest_location = location
        print(seed, location, lowest_location)
        seed += 1

print(lowest_location)

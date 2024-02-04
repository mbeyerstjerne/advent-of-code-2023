import re

engine_schematic = []

with open('day_03/day_03_input.txt', 'r') as f:
    for i, line in enumerate(f):
        engine_schematic.append(line.strip())

sum = 0

for index, line in enumerate(engine_schematic):
    matches = re.finditer(r'[0-9]+', line)
    for item in matches:
        up_adjacent_squares = engine_schematic[max(0,index-1)][item.start()-1:item.end()+1]
        middle_adjacent_squares = line[max(0,item.start()-1):min(item.end()+ 1, len(line))]
        down_adjacent_squares = engine_schematic[min(len(engine_schematic)-1,index+1)][item.start()-1:item.end()+1:]
        if any(re.search(r'[^0-9\.\n]',square_rows) for square_rows in [up_adjacent_squares, middle_adjacent_squares, down_adjacent_squares]):
            sum += int(item.group())
        else:
            continue

print(sum)
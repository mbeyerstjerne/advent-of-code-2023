import re

colour_regex = { #setting up regex search patterns
    'red': r'[0-9]+\s\bred\b',
    'green': r'[0-9]+\s\bgreen\b',
    'blue': r'[0-9]+\s\bblue\b'
}

colour_max = { #setting up the maximum value of cubes
    'red': 12,
    'green': 13,
    'blue': 14
}

def game_possible_value(line): #runs through each colour, pulls out matches with number values
    for colour in colour_regex:
        matches = re.findall(colour_regex[colour], line)
        for item in matches:
            if int(item.split()[0]) > colour_max[colour]:   #if an instance is found where nr of cubes goes over max, returns 0
                return 0
            else:
                continue                                    #if no instance is found, continue onto next item in matches, and next colour
    return int(re.search(r'Game (\d+)', line).group(1))

sum = 0

with open('day_02/day_02_input.txt', 'r') as f:
    for line in f:
        sum = sum + game_possible_value(line)

print(sum)
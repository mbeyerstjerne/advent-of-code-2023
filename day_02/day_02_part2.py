import re

colour_regex = { #setting up regex search patterns
    'red': r'[0-9]+\s\bred\b',
    'green': r'[0-9]+\s\bgreen\b',
    'blue': r'[0-9]+\s\bblue\b'
}

def game_power(line): #runs through each colour, pulls out matches with number values
    colour_minimum = {'red': 0, 'green': 0, 'blue': 0 }
    for colour in colour_regex:
        matches = re.findall(colour_regex[colour], line)
        for item in matches:
            if int(item.split()[0]) > colour_minimum[colour]:   #if a instance with 'higher' number of cubes is found, that is set as the minimum of cubes needed
                colour_minimum[colour] = int(item.split()[0])
            else:
                continue                                    #if no instance is found, continue onto next item in matches, and next colour
    return colour_minimum['blue'] * colour_minimum['green'] * colour_minimum['red'] #returns power of the set

sum = 0

with open('day_02/day_02_input.txt', 'r') as f:
    for line in f:
        sum = sum + game_power(line)

print(sum)
import re

number_words = { 
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

sum = 0

with open('day_01\day_01_input.txt','r') as f:
    for line in f:
        num = ''
        line_purenumbers = ['_' for _ in range(len(line))]      #Creating a 'mock' line to be able to imprint the found numerical digits later on
        for match in re.finditer(r'\d', line):                  #Two matches are made, this first one is for a single digit
            line_purenumbers[match.start()] = match.group()     #Matches that are found replace the value list of the 'mock' line
        for number in number_words:
            for match in re.finditer(number, line):             #Second match checks for words that appear according to the number_words dict
                line_purenumbers[match.start()] = number_words[match.group()]      #Any matches that are found, their numerical equivalent is recorded in the first index position
        num = ''.join(str(v) for v in line_purenumbers if v != '_')  #Concatenating the list together as a string and removing the 'dud' values
        sum = sum + 10*int(num[0])+int(num[::-1][0])            #Using the same command in part 1 to find the calibration value.

print(sum)
sum = 0

with open('day_01\day_01_input.txt','r') as f:
    for line in f:
        num = ''
        for c in line:                                  #Iterate through each character in a line
            if c.isdigit():                             #If a character is a digit,
                num = num + c                           #Since the characters are in string format, they are added/concatenated onto object num
        sum = sum + 10*int(num[0])+int(num[::-1][0])    #Taking the sum of the first digit as the tens value and the last as the ones.

print(sum)
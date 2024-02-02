sum = 0

with open('day_01\day_01_input.txt','r') as f:
    for line in f:
        num = ''
        for c in line:
            if c.isdigit():
                num = num + c
        sum = sum + 10*int(num[0])+int(num[::-1][0])

print(sum)
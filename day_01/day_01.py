import re

sum=0
groups=[]

with open("day_01_input.txt", "r") as f:
    for line in f: 
        print(f.readline(1))

'''
        first = re.search(r'\d+', line)
        last = re.search(r'\d+', line[::-1])
        calibration = 10*first + 1*last
        groups.append(calibration)

calibration_total = groups.sum()

calibration_total
'''
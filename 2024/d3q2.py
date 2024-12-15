import re

d=None
with open("d3q1.txt") as f:
    d = f.read()

p = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

data = re.findall(p, d)

t = 1
s = 0
for x in data:
    if x[0] == 'do()':
        t = 1
    elif x[0] == 'don\'t()':
        t = 0
    elif t:
        s += int(x[1]) * int(x[2])

print(s)
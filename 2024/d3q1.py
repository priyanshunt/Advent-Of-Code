import re

d=None
with open("d3q1.txt") as f:
    d = f.read()

p = r"mul\((\d+),(\d+)\)"

data = re.findall(p, d)

s = 0
for x, y in data:
    s += int(x)*int(y)

print(s)
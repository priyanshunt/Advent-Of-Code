d = []
with open("d12.txt", 'r') as f:
    d = [x.strip() for x in f.readlines()]

patterns = []
regions = []
for i in range(0, len(d), 5):
    if d[i+4] == "":
        patterns.append(d[i+1:i+4])
    else:
        break

for x in d:
    if 'x' in x:
        a, b = x.split(': ')
        regions.append(list(map(int, a.split('x'))) +
                       [list(map(int, b.split(' ')))])

c = 0
for x in regions:
    s = 0
    for y in x[2]:
        s += y * 9
    if x[0] * x[1] >= s:
        c += 1

print(c)

d = None
with open("d5.txt", 'r') as f:
    d = [x.strip() for x in f.readlines()]

i = d.index('')
d1 = d[:i]
d2 = d[i+1:]

c = 0
for x in d2:
    x = int(x)
    for y in d1:
        y1, y2 = map(int, y.split('-'))
        if x >= y1 and x <= y2:
            c += 1
            break

print(c)

d = None
with open("d2.txt", 'r') as f:
    d = f.read().split(',')

s = 0

for x in d:
    start, end = list(map(int, x.split('-')))
    for y in range(start, end + 1):
        y = str(y)
        l = len(y)
        if y[:l//2] == y[l//2:]:
            s += int(y)

print(s)

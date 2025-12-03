d = None
with open("d2.txt", 'r') as f:
    d = f.read().split(',')

s = 0

for x in d:
    start, end = list(map(int, x.split('-')))
    for y in range(start, end + 1):
        y = str(y)
        l = len(y)
        for z in range(1, l//2 + 1):
            if (len(y.split(y[:z])) - 1) * z == l:
                s += int(y)
                break

print(s)

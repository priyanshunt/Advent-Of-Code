d = None
with open("d9.txt", 'r') as f:
    d = [list(map(int, x.strip().split(','))) for x in f.readlines()]

area = 0
for x in d:
    for y in d:
        a = abs(x[0] - y[0] + 1) * abs(x[1] - y[1] + 1)
        if a > area:
            area = a

print(area)

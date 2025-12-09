d = None
with open("d9.txt", 'r') as f:
    d = [list(map(int, reversed(x.strip().split(',')))) for x in f.readlines()]

d1 = [['.' for _ in range(14)] for _ in range(10)]

x1, y1 = d[-1]
for z in d:
    x2, y2 = z
    print((x1, y1), (x2, y2))
    if x1 == x2:
        a, b = y1, y2
        if a > b:
            a, b = b, a
        for z in range(a, b + 1):
            d1[x1][z] = 'X'
    else:
        a, b = x1, x2
        if a > b:
            a, b = b, a
        for z in range(a, b + 1):
            d1[z][y1] = 'X'
    x1, y1 = x2, y2

    for x in d1:
        print(''.join(x))

# for x in d1:
#     print(''.join(x))

d = []
with open("d11.txt", 'r') as f:
    d = [x.strip().split(' ') for x in f.readlines()]
    d1 = {x[0][:-1]: x[1:] for x in d}


def rec(d, start, end):
    if d[start][0] == end:
        return 1

    s = 0

    for x in d[start]:
        s += rec(d, x, end)

    return s


print(rec(d1, 'you', 'out'))

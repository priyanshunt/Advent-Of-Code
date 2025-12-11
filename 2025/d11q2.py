d = []
with open("d11.txt", 'r') as f:
    d = [x.strip().split(' ') for x in f.readlines()]
    d1 = {x[0][:-1]: x[1:] for x in d}


def rec(d, start, end, c, v):
    if start in v[c]:
        return v[c][start]
    elif d[start][0] == end:
        if "dac" in c and "fft" in c:
            return 1
        else:
            return 0
    elif start == "dac" and "dac" not in c:
        c = "dac" + c
    elif start == "fft" and "fft" not in c:
        c += "fft"

    s = 0

    for x in d[start]:
        s += rec(d, x, end, c, v)

    v[c][start] = s

    return s


print(rec(d1, 'svr', 'out', "", {"": {}, "dac": {}, "fft": {}, "dacfft": {}}))

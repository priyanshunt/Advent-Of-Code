d = None
with open("d21q1.txt") as f:
    d = f.read().split('\n')

nk = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['X', '0', 'A']]
nkp = dict((j,(x, y)) for x, i in enumerate(nk) for y, j in enumerate(i))
dk = [['X', '^', 'A'], ['<', 'v', '>']]
dkp = dict((j,(x, y)) for x, i in enumerate(dk) for y, j in enumerate(i))

def func(d, k, kp):
    d1 = []
    i, j = kp['A']
    for x in d:
        p = ''
        for y in x:
            i1, j1 = kp[y]
            id, jd = i1 - i, j1 - j
            pi = "v"*id+"^"*-id
            pj = ">"*jd+"<"*-jd
            if id == 0 or jd == 0:
                p += pj + pi
            else:
                if jd > 0 and k[i1][j] != 'X':
                    p += pi + pj
                elif id < 0 and k[i][j1] != 'X':
                    p += pj + pi
                elif k[i][j1] != 'X':
                    p += pj + pi
                elif k[i1][j] != 'X':
                    p += pi + pj
            i, j = i1, j1
            p += 'A'
        d1.append(p)
    print(d1)
    return d1

d1 = func(d, nk, nkp)
d2 = func(d1, dk, dkp)
d3 = func(d2, dk, dkp)

s = 0
for x, y in zip(d, d3):
    s += int(x[:-1]) * len(y)
print(s)
d = None
with open("d21q1.txt") as f:
    d = f.read().split('\n')

nk = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['X', '0', 'A']]
nkp = dict((j,(x, y)) for x, i in enumerate(nk) for y, j in enumerate(i))
dk = [['X', '^', 'A'], ['<', 'v', '>']]
dkp = dict((j,(x, y)) for x, i in enumerate(dk) for y, j in enumerate(i))

t = 0
def func(start, end, k, kp):
    i, j = kp[start]
    i1, j1 = kp[end]
    id, jd = i1 - i, j1 - j

    p = ''
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
    return p

d1 = []
for x in d:
    start = 'A'
    s = {}
    for y in x:
        c = func(start, y, nk, nkp)
        if c in s:
            s[c] += 1
        else:
            s[c] = 1
        start = y
    d1.append(s)

move = ['<', '>', 'v', '^', 'A']
move_cache = {}
for x in move:
    for y in move:
        move_cache[x + y] = func(x, y, dk, dkp)

s = None
for _ in range(25):
    d2 = []
    s = []
    for x in d1:
        x1 = {}
        for k, v in x.items():
            k = 'A' + k
            for i in range(len(k) - 1):
                ele = move_cache[k[i:i+2]]
                if ele in x1:
                    x1[ele] += v
                else:
                    x1[ele] = v
        s.append(sum([len(k) * v for k, v in x1.items()]))
        d2.append(x1)
    d1 = d2

s1 = 0
for x, y in zip(d, s):
    s1 += int(x[:-1]) * y
print(s1)
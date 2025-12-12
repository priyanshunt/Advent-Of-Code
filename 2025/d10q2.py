from z3 import Solver, Int, Sum, sat

bw = []
jr = []
with open("d10.txt", 'r') as f:
    d = [x.strip().split(' ') for x in f.readlines()]
    for x in d:
        bw.append([tuple(map(int, y[1:-1].split(','))) for y in x[1:-1]])
        jr.append(list(map(int, x[-1][1:-1].split(','))))

c = 0
for bwi, jri in zip(bw, jr):

    s = Solver()
    v = [Int(f"a{i}") for i in range(len(bwi))]
    for v1 in v:
        s.add(v1 >= 0)

    for i, x in enumerate(jri):
        v1 = [v[j] for j, b in enumerate(bwi) if i in b]
        s.add(Sum(v1) == x)

    while s.check() == sat:
        model = s.model()
        n = sum([model[d].as_long() for d in model])
        s.add(Sum(v) < n)

    c += n

print(c)

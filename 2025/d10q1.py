il = []
bw = []
jr = []
with open("d10.txt", 'r') as f:
    d = [x.strip().split(' ') for x in f.readlines()]
    for x in d:
        il.append(list(x[0][1:-1]))
        bw.append([tuple(map(int, y[1:-1].split(','))) for y in x[1:-1]])
        # jr.append(tuple(map(int, x[-1][1:-1].split(','))))


def subsets(arr):
    res = []

    def backtrack(i, current):
        if i == len(arr):
            res.append(current[:])
            return
        backtrack(i + 1, current)
        current.append(arr[i])
        backtrack(i + 1, current)
        current.pop()

    backtrack(0, [])
    return res


s = 0
for i in range(len(il)):
    x = il[i]
    y = bw[i]
    # z = jr[i]

    res = subsets([j for j in range(len(y))])
    res.sort(key=lambda x: len(x))

    for a in res:
        c = ['.' for _ in range(len(x))]

        for b in a:
            for g in y[b]:
                if c[g] == '.':
                    c[g] = '#'
                else:
                    c[g] = '.'

        f = True
        for d, e in zip(x, c):
            if d != e:
                f = False
                break

        if f:
            s += len(a)
            break

print(s)

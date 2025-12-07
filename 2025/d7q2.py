d = None
with open("d7.txt", 'r') as f:
    d = [list(x.strip()) for x in f.readlines()]

d1 = {(1, d[0].index('S')): 1}
for i in range(2, len(d)):
    d2 = {}
    for x, c in d1.items():
        i, j = x
        i += 1
        if d[i][j] == '^':
            if j-1 >= 0 and d[i][j-1] == '.':
                if (i, j-1) in d2:
                    d2[(i, j-1)] += c
                else:
                    d2[(i, j-1)] = c
            if j+1 < len(d[i]) and d[i][j+1] == '.':
                if (i, j+1) in d2:
                    d2[(i, j+1)] += c
                else:
                    d2[(i, j+1)] = c
        else:
            if (i, j) in d2:
                d2[(i, j)] += c
            else:
                d2[(i, j)] = c
    d1 = d2

print(sum(d1.values()))

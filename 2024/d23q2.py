d = None
with open("d23q1.txt") as f:
    d = f.read().split('\n')

d1 = []
for x in d:    
    d1.append(x.split('-'))
d = d1

while True:
    d2 = []
    for x in d1:
        conn = {}
        for y in d:
            if y[0] in x:
                if y[1] in conn:
                    conn[y[1]] += 1
                    if conn[y[1]] == len(x):
                        s = set(x)
                        s.add(y[1])
                        if len(s) == len(x) + 1 and s not in d2:
                            d2.append(s)
                else:
                    conn[y[1]] = 1
            elif y[1] in x:
                if y[0] in conn:
                    conn[y[0]] += 1
                    if conn[y[0]] == len(x):
                        s = set(x)
                        s.add(y[0])
                        if len(s) == len(x) + 1 and s not in d2:
                            d2.append(s)
                else:
                    conn[y[0]] = 1

    if len(d2) == 1:
        print(','.join(sorted(list(d2[0]))))
        break
    d1 = d2
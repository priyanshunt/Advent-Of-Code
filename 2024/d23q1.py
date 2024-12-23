d = None
with open("d23q1.txt") as f:
    d = f.read().split('\n')

conn = {}
for x in d:    
    if x[0] == 't' or x[3] == 't':
        conn[x] = []

for x in d:
    for k in conn:
        if (k[:2] == x[:2] or k[:2] == x[3:] or k[3:] == x[:2] or k[3:] == x[3:]) and k != x:
            conn[k].append(x)

l = []
for k, v in conn.items():
    three = {}
    for val in v:
        s = 0
        if val[:2] == k[:2] or val[:2] == k[3:]:
            if val[3:] in three:
                s = {val[:2], val[3:], k[:2], k[3:]}
                if s not in l:
                    l.append(s)
            else:
                three[val[3:]] = 1
        elif val[3:] == k[:2] or val[3:] == k[3:]:
            if val[:2] in three:
                s = {val[:2], val[3:], k[:2], k[3:]}
                if s not in l:
                    l.append(s)
            else:
                three[val[:2]] = 1

print(len(l))
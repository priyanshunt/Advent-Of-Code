d = None
with open("d22q1.txt") as f:
    d = f.read().split('\n')

data = [int(x) for x in d]

l = []
for x in data:
    l1 = [x%10]
    for _ in range(2000):
        x = ((x * 64) ^ x) % 16777216
        x = ((x // 32) ^ x) % 16777216
        x = ((x * 2048) ^ x) % 16777216
        l1.append(x%10)
    l.append(l1)

d = {}
for x in l:
    seq = []
    for i in range(4,2001):
        s = ''
        for j in range(4):
            s += str(x[i + j - 3] - x[i + j - 4])
        if s not in seq:
            seq.append(s)
            if s in d:
                d[s].append(x[i])
            else:
                d[s] = [x[i]]

m = 0
for x in d.values():
    s = sum(x)
    if m < s:
        m = s
print(m)
d = None
with open("d3.txt", 'r') as f:
    d = [x.strip() for x in f.readlines()]

s = 0
for x in d:
    l = [y for y in x[:12]]
    for i in range(12, len(x)):
        for j in range(11):
            if l[j] < l[j+1]:
                l = l[:j] + l[j+1:] + [x[i]]
                break
        if l[11] < x[i]:
            l = l[:11] + [x[i]]
    s += int(''.join(l))

print(s)

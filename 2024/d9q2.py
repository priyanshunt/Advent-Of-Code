d = None
with open("d9q1.txt") as f:
    d = list(f.read() + '0')

j = 0
d1 = []
for i in range(0, len(d), 2):
    d1 += [[str(j)] * int(d[i])] + [['.'] * int(d[i+1])]
    j += 1

d1 = [x for x in d1 if x != []]
l = len(d1)
j = l - 1
while(j >= 0):
    if d1[j][0] != '.':
        for i in range(j):
            if d1[i][0] == '.' and len(d1[j]) <= len(d1[i]):
                diff = len(d1[i]) - len(d1[j])
                t = d1[j]
                d1[j] = ['.'] * len(d1[j])
                if diff > 0:
                    d1[i] = d1[i][:diff]
                    d1.insert(i, t)
                    j += 1
                    l += 1
                else:
                    d1[i] = t
                break
    j -= 1

d2 = sum(d1, [])
s = 0
for i in range(len(d2)):
    if d2[i] != '.':
        s += i * int(d2[i])
print(s)
d = None
with open("d9q1.txt") as f:
    d = list(f.read() + '0')

j = 0
d1 = []
for i in range(0, len(d), 2):
    d1 += [str(j)] * int(d[i]) + ['.'] * int(d[i+1])
    j += 1

dot = d1.count('.')
l = len(d1)
j = l - 1
for i in range(l - dot):
    if d1[i] == '.':
        while(d1[j] == '.'):
            j -= 1        
        t = d1[i]
        d1[i] = d1[j]
        d1[j] = t

s = 0
for i in range(l-dot):
    s += i * int(d1[i])
print(s)
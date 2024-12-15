d = None
with open("d7q1.txt") as f:
    d = f.read().split('\n')

data = [x.split(': ') for x in d]

for i in range(len(data)):
    data[i] = (int(data[i][0]), tuple(map(int, data[i][1].split(' '))))

def func(l, i, s, t):
    if i == len(l):
        if t == s:
            return True
        return False
    return func(l, i+1, s+l[i], t) or func(l, i+1, s*l[i], t)
    
s = 0
for x in data:
    t = x[0]
    l = x[1]
    if func(l, 1, l[0], t):
        s += t
print(s)
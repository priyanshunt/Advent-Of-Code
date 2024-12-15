d= None
with open("d10q1.txt") as f:
    d = f.read().split('\n')

data = [[int(y) for y in x] for x in d]

l = len(data)
l1 = len(data[0])

def func(p, v):
    r,c = p
    if 0 <= r < l and 0 <= c < l1:
        if data[r][c] == v:
            if v == 9:
                return 1
            else: 
                return func((r + 1, c), v + 1) + func((r - 1, c), v + 1) + func((r, c + 1), v + 1) + func((r, c - 1), v + 1)
        
    return 0
    
s = 0
for i in range(l):
    for j in range(l1):
        if data[i][j] == 0:
            s += func((i, j), 0)
print(s)
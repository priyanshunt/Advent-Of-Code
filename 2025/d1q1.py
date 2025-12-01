d = []
with open("d1.txt", 'r') as f:
    d = f.readlines()

s = 50
c = 0
for x in d:
    if x[0] == 'L':
        s -= int(x[1:])
    else:
        s += int(x[1:])
    s %= 100
    if s == 0:
        c += 1

print(c)

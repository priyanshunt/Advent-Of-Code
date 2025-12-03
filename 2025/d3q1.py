d = None
with open("d3.txt", 'r') as f:
    d = [x.strip() for x in f.readlines()]

s = 0
for x in d:
    p = int(x[0])
    q = int(x[1])
    for i in range(2, len(x)):
        if p < int(x[i - 1]):
            p = int(x[i - 1])
            q = int(x[i])
        elif q < int(x[i]):
            q = int(x[i])
    s += p * 10 + q

print(s)

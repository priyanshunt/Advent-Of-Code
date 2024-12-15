import numpy as np

d = None
d1 = None
with open("d5q1.txt") as f:
    d = f.read().split("\n")

    a = np.array(d)
    i = np.where(a == '')[0]
    d1 = np.split(a, i + 1)
    d1 = [list(x[x != '']) for x in d1]
    
    d = d1[0]
    d1 = d1[1]

rules = []
for rule in d:
    rules.append(list(map(int, rule.split('|'))))

sum = 0
for i in range(len(d1)):
    d2 = d1[i].split(',')
    t = 0
    for j in range(len(d2) - 1):
        for k in range(j + 1, len(d2)):
            if [int(d2[k]), int(d2[j])] in rules:
                t = 1
                c = d2[k]
                d2[k] = d2[j]
                d2[j] = c    
    if t == 1:
        sum += int(d2[len(d2)//2])

print(sum)
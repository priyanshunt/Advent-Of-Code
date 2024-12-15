data = []
d=None
with open("d2q1.txt") as f:
    d = f.readlines()

for x in d:
    data.append([int(num) for num in x.split()])

count = 0

for x in data:
    prev = x[0]
    t = 0
    for y in x[1:]:
        if y - prev < 1 or y - prev > 3:
            t = 1
            break
        prev = y
    print(t)
    if t == 0:
        count += 1

for x in data:
    prev = x[0]
    t = 0
    for y in x[1:]:
        if prev - y < 1 or prev - y > 3:
            t = 1
            break
        prev = y

    if t == 0:
        count += 1

print(count)
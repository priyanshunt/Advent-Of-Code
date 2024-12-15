data = []
d=None
with open("d2q1.txt") as f:
    d = f.readlines()

for x in d:
    data.append([int(num) for num in x.split()])

def is_valid(x):
    prev = x[0]
    t = 0
    for y in x[1:]:
        if y - prev < 1 or y - prev > 3:
            t = 1
            break
        prev = y
    if t == 0:
        return True

    prev = x[0]
    t = 0
    for y in x[1:]:
        if prev - y < 1 or prev - y > 3:
            t = 1
            break
        prev = y

    if t == 0:
        return True
    
    return False

count = 0

for x in data:
    if is_valid(x):
        count += 1
        continue
    else:
        for i in range(len(x)):
            if is_valid(x[:i] + x[i+1:]):
                print(x)
                count += 1
                break

print(count)
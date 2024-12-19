d = None
with open("d19q1.txt") as f:
    d = f.read().split('\n')

pattern = d[0].split(', ')
design = d[2:]

towel = {}
def func(design):
    if design in towel:
        c = towel[design]
    else:
        c = 0
        if design == "":
            c = 1
        else:
            for x in pattern:
                if design.startswith(x):
                    c += func(design[len(x):])
        towel[design] = c
    return c

c = 0
for x in design:
    c += func(x)
print(c)
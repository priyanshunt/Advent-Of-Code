d = None
with open("d24q1.txt") as f:
    d = f.read().split('\n')

wire = {}
for i in range(d.index('')):
    x = d[i].split(': ')
    wire[x[0]] = int(x[1])
equation = [x.split(' ') + [0] for x in d[d.index('')+1:]]

i = len(wire)
l = i + len(equation)

while i < l:
    for j in range(len(equation)):
        x = equation[j]
        wire1 = x[0]
        gate = x[1]
        wire2 = x[2]
        wire3 = x[4]
        flag = x[5]
        if flag == 0 and wire1 in wire and wire2 in wire:
            equation[j][5] = 1
            i += 1
            if gate == 'XOR':
                wire[wire3] = wire[wire1] ^ wire[wire2]
            elif gate == 'AND':
                wire[wire3] = wire[wire1] & wire[wire2]
            elif gate == 'OR':
                wire[wire3] = wire[wire1] | wire[wire2]

i = 0
s = ''
while True:
    x = f'z{i:02}'
    if x in wire:
        s = str(wire[x]) + s
        i += 1
    else:
        break

print(int(s, 2))
d = None
with open("d17q1.txt") as f:
    d = f.read().split('\n')

def func(a):
    b = 0
    c = 0
    ins = [int(x) for x in d[4].split(' ')[1].split(',')]

    i = 0
    l = len(ins)

    def func(operand):
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        return operand

    out = []

    while i < l:
        opcode = ins[i]
        operand = ins[i + 1]
        combo_operand = func(operand)
        if opcode == 0:
            a = a // (2 ** combo_operand)
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = combo_operand % 8
        elif opcode == 3:
            if a != 0:
                i = operand
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            out.append(combo_operand % 8)
        elif opcode == 6:
            b = a // (2 ** combo_operand)
        elif opcode == 7:
            c = a // (2 ** combo_operand)
        i += 2

    return ','.join([str(x) for x in out])

ins = d[4].split(' ')[1]

j = 7
k = 1
l = []
while (True):
    val = str(func(j))
    if ins == val:
        print(j)
        break
    elif ins.endswith(val):
        j *= 8
    else:
        j += 1
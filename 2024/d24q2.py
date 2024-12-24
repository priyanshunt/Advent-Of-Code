d = None
with open("d24q1.txt") as f:
    d = f.read().split('\n')

l = d.index('') // 2
equation = {}
for i in range(d.index('') + 1, len(d)):
    x = d[i].split(' ')
    equation[x[4]] =  (x[0], x[1], x[2])

output = {v: k for k, v in equation.items()}

i = 1
incorrect = []
while i < l:

    x = f'x{i:02}'
    y = f'y{i:02}'
    z = f'z{i:02}'

    input_xor = (x, 'XOR', y)
    output_xor = None
    if input_xor not in output:
        input_xor = (y, 'XOR', x)
    output_xor = output[input_xor]
    
    input_and = (x, 'AND', y)
    output_and = None
    if input_and not in output:
        input_and = (y, 'AND', x)
    output_and = output[input_and]
    
    eq_z = equation[z]

    if 'AND' in eq_z:
        incorrect.append(z)
        if output_and.startswith('z') and output_and[1:].isnumeric():
            for k, v in output.items():
                if output_xor in k and 'XOR' in k:
                    incorrect.append(v)
                    output[input_and] = v
                    output[k] = z
                    break
        else:
            for k, v in output.items():
                if eq_z[0] in k and 'XOR' in k:
                    incorrect.append(v)
                    output[eq_z] = v
                    output[k] = z
                    break
    
    if 'OR' in eq_z:
        incorrect.append(z)
        for k, v in output.items():
            if (eq_z[0] == v or eq_z[2] == v) and 'AND' in k and not x in k:
                t = (k[0], 'XOR', k[2])
                incorrect.append(output[t])
                output[eq_z] = output[t]
                output[t] = z
                break
    
    if output_xor not in eq_z and output_and in eq_z and 'XOR' in eq_z:
        incorrect.append(output_xor)
        incorrect.append(output_and)
        output[input_xor], output[input_and] = output[input_and], output[input_xor]

    i += 1

equation = {v: k for k, v in output.items()}

print(','.join(sorted(incorrect)))
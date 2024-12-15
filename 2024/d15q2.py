d = None
with open("d15q1.txt") as f:
    d = f.read().split('\n')

t = 0
data = [[], []]
for x in d:
    if x == '':
        t = 1
        continue
    data[t].append(x)

m = ''.join(data[1])
data = [list(x) for x in data[0]]
new_data = []

for x in data:
    d2 = []
    for y in x:
        if y=='#':
            d2.append('#')
            d2.append('#')
        if y=='O':
            d2.append('[')
            d2.append(']')
        if y=='.':
            d2.append('.')
            d2.append('.')
        if y=='@':
            d2.append('@')
            d2.append('.')
    new_data.append(d2)

data = new_data
l = len(data)
l1 = len(data[0])

pos = None
for i in range(l):
    for j in range(l1):
        if data[i][j] == '@':
            pos = (i, j)
            break

d = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

print('Initial')
for i in range(l):
    for j in range(l1):
        print(data[i][j], end='')
    print('')
print('----------------', end='\n\n')

for x in m:
    y = d[x]
    pos1 = (pos[0] + y[0], pos[1] + y[1])

    if x == '<' or x == '>' or data[pos1[0]][pos1[1]] == '#' or data[pos1[0]][pos1[1]] == '.':
        move_pos = [pos]
        move_ele = ['@']
        t = 0
        while data[pos1[0]][pos1[1]] != '#' and t == 0:
            move_pos.append(pos1)
            if data[pos1[0]][pos1[1]] == '.':
                move_ele.insert(0, '.')
                pos = move_pos[1]
                t = 1
                break
            else:
                move_ele.append(data[pos1[0]][pos1[1]])
                pos1 = (pos1[0] + y[0], pos1[1] + y[1])
        
        if t == 1:            
            for p, e in zip(move_pos, move_ele):
                data[p[0]][p[1]] = e
        
        # print(x)
        # for i in range(l):
        #     for j in range(l1):
        #         print(data[i][j], end='')
        #     print('')
        # print('----------------', end='\n\n')
    else:
        
        to_move = [(pos, data[pos[0]][pos[1]])]
        l2 = len(to_move)
        i = 0
        t = 0

        while i < l2:
            to_move_pos = to_move[i][0]
            # print(i, l2, to_move_pos)
            pos1 = (to_move_pos[0] + y[0], to_move_pos[1] + y[1])
            if data[to_move_pos[0]][to_move_pos[1]] == '.':
                pass
            elif data[pos1[0]][pos1[1]] == '#':
                t = 1
                break
            elif data[pos1[0]][pos1[1]] == '[':
                if (pos1, data[pos1[0]][pos1[1]]) not in to_move:
                    to_move.append((pos1, data[pos1[0]][pos1[1]]))
                    l2 +=1
                if ((pos1[0], pos1[1] + 1), data[pos1[0]][pos1[1] + 1]) not in to_move:
                    to_move.append(((pos1[0], pos1[1] + 1), data[pos1[0]][pos1[1] + 1]))
                    l2 += 1
            elif data[pos1[0]][pos1[1]] == ']':
                if (pos1, data[pos1[0]][pos1[1]]) not in to_move:
                    to_move.append((pos1, data[pos1[0]][pos1[1]]))
                    l2 +=1
                if ((pos1[0], pos1[1] - 1), data[pos1[0]][pos1[1] - 1]) not in to_move:
                    to_move.append(((pos1[0], pos1[1] - 1), data[pos1[0]][pos1[1] - 1]))
                    l2 += 1
            else:
                to_move.append((pos1, data[pos1[0]][pos1[1]]))
                l2 += 1
            i += 1
        
            # print(to_move, t)

        if t == 0:
            pos = (pos[0] + y[0], pos[1] + y[1])
            new_di = {}
            l3 = len(to_move)
            sep_list = []
            sel_pos = None
            
            while l3 > 0:
                if sel_pos == None:
                    sel_pos = to_move[0][0]
                    sep_list.append([to_move.pop(0)])
                    l3 -= 1
                else:
                    t1 = 0
                    sel_pos = (sel_pos[0] + y[0], sel_pos[1] + y[1])
                    for z in to_move:
                        if z[0] == sel_pos:
                            t1 = 1
                            sep_list[-1].append(z)
                            to_move.remove(z)
                            l3 -= 1
                            break
                    if t1 == 0:
                        sel_pos = None

            # print(sep_list)

            for i in range(len(sep_list)):
                for j in range(len(sep_list[i])):
                    
                    if j + 1 == len(sep_list[i]):
                        p = sep_list[i][0][0]
                        e = '.'
                    else:
                        p = sep_list[i][j + 1][0]
                        e = sep_list[i][j][1]
                    data[p[0]][p[1]] = e
                    

        
        # print(x)
        # for i in range(l):
        #     for j in range(l1):
        #         print(data[i][j], end='')
        #     print('')
        # print('----------------', end='\n\n')


print('Final')
for i in range(l):
    for j in range(l1):
        print(data[i][j], end='')
    print('')
print('----------------', end='\n\n')

s = 0
for i in range(l):
    for j in range(l1):
        if data[i][j] == '[':
            s += 100 * i + j
print(s)
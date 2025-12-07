d = None
with open("d7.txt", 'r') as f:
    d = [list(x.strip()) for x in f.readlines()]

d[1][d[0].index('S')] = '|'
c = 0
for i in range(2, len(d)):
    for j in range(len(d[i])):
        if d[i-1][j] == '|':
            if d[i][j] == '^':
                c += 1
                if j-1 >= 0 and d[i][j-1] == '.':
                    d[i][j-1] = '|'
                if j+1 < len(d[i]) and d[i][j+1] == '.':
                    d[i][j+1] = '|'
            else:
                d[i][j] = '|'

print(c)

bw = []
jr = []
with open("d9.txt", 'r') as f:
    d = [x.strip().split(' ') for x in f.readlines()]
    for x in d:
        bw.append([tuple(map(int, y[1:-1].split(','))) for y in x[1:-1]])
        jr.append(list(map(int, x[-1][1:-1].split(','))))

s = {}
l = None

def rec(bw, jr, i, cost):
    if jr.count(-1) > 0 or tuple(jr) in s and s[tuple(jr)] < cost:
        pass
    else:
        s[tuple(jr)] = cost
        if i < l:
            jr1 = jr.copy()
            for x in bw[i]:
                jr1[x] -= 1
            rec(bw, jr1, i, cost + 1)
            rec(bw, jr.copy(), i + 1, cost)

c = 0
for i in range(len(bw)):
    
    s = {}
    l = len(bw[i])
    rec(sorted(bw[i], key = lambda x:len(x), reverse=True), jr[i], 0, 0)
    
    c += s[tuple([0 for _ in range(len(jr[i]))])]
    print(i, c)

print(c)

d= None
with open("d11q1.txt") as f:
    d = list(map(int, f.read().split(' ')))

t = 75

num = {}
def func(x, t):
    if (x, t) not in num:
        c = None
        if t > 0:
            if x == 0:
                c = func(1, t - 1)
            elif len(str(x)) % 2 == 0:
                mid = len(str(x)) // 2
                left = int(str(x)[:mid])
                right = int(str(x)[mid:])
                c = func(left, t - 1) + func(right, t - 1)
            else:
                c = func(x * 2024, t - 1)
        else:
            c = 1
        num[(x, t)] = c
        return c
    else:
        return num[(x, t)]

s = 0
for x in d:
    s += func(x, t)

print(s)
            

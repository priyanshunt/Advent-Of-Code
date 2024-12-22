d = None
with open("d22q1.txt") as f:
    d = f.read().split('\n')

data = [int(x) for x in d]

s = 0
for x in data:
    y = x
    for _ in range(2000):
        x = ((x * 64) ^ x) % 16777216
        x = ((x // 32) ^ x) % 16777216
        x = ((x * 2048) ^ x) % 16777216
    s += x

print(s)
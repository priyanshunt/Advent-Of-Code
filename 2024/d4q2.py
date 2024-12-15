d = None
with open("d4q1.txt") as f:
    d = f.read().split('\n')

data = [list(x) for x in d]

l = len(data)
l1 = len(data[0])
c = 0
options = ["MAS", "SAM"]

for i in range(l):
    for j in range(l1):
        if data[i][j]== 'A' and i + 1 < l and i - 1 >= 0 and j + 1 < l1 and j - 1 >= 0:
            x = data[i-1][j-1] + data[i][j] + data[i + 1][j + 1]
            y = data[i-1][j+1] + data[i][j] + data[i + 1][j - 1]

            if x in options and y in options:
                c += 1

print(c)
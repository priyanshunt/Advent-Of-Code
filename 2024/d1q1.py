data1=[]
data2=[]
d=None
with open("d1q1.txt") as f:
    d = f.readlines()

for x in d:
    y = x.split('   ')
    data1.append(int(y[0]))
    data2.append(int(y[1]))

data1.sort()
data2.sort()

diff = 0
for x,y in zip(data1, data2):
    diff += abs(x-y)

print(diff)
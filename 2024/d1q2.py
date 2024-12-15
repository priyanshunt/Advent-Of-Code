data1=[]
data2=[]
d=None
with open("d1q1.txt") as f:
    d = f.readlines()

di = {}
for x in d:
    y = x.split('   ')
    data1.append(int(y[0]))
    data2.append(int(y[1]))

diff = 0
for x in data1:
    diff += x * data2.count(x)

print(diff)
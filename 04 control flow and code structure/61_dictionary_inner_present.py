w = ['mon', 'tue', 'wed']
f = ['coffe', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

print("#########################")

d = {x: y for x, y in zip(w, f)}

print(d)

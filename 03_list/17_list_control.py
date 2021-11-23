l = [1, 2, 3, 4, 5]

print(l[0])

print(l[-1])
print(l[-2])

print(l[2:])
print(l[:])
print(l[-0])

l[2:3] = [4,5]
print(l)

l.append(100)
print(l)

l.insert(0,200)
print(l)

print(l.pop())

del l[0]
print(l)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(a)
print(b)

a += b

print(a)

x = [i for i in range(1,6)]
y = [i for i in range(6,11)]

print(x, y)

x.extend(y)
print(x)

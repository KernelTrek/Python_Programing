def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


g = (i for i in range(10))
print(type(g))

print(next(g))

# tuple 로 하고싶은 경우

g = tuple(i for i in range(10))
print(type(g))
print(g)
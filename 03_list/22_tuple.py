t = (1, 2, 3, 4, 1, 2)
print(t)

print(type(t))

# 튜플은 수정이 안된다. 그래서 아래 코드는 에러
# t[0] = 100

print(t[0])
print(t[-1])

print(t.index(1))

print(t.index(1, 2))

t = ([1, 2, 3], [4, 5, 6])
print(t)

print(t[0][0])
t[0][0] = 100
print(t)
i = [i for i in range(1, 6)]
j = i
print("i =", i)
print("j =", j)

# 참조 전달
j[0] = 100
print("i =", i)
print("j =", j)

# 값의 의한 전달
x = [1, 2, 3, 4, 5]
y = x.copy()

y[0] = 100
print("x =", x)
print("y =", y)

X = 20
Y = X
Y = 5

print(id(X))
print(id(Y))
print(Y)
print(X)

X = ['a' , 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)





a = {1, 2, 2, 3, 4, 4, 5}
# 중복된 값이 사라짐
print(a)

# 형태는 set
print(type(a))

b = {2, 3, 3, 6, 7}
print(b)

print(type(b))

# a에 있는 요소중 b 의 요소를 뺀것
print(a - b)
print(b - a)

# 교집합 하는 법
print(a & b)

print(a | b)

# a 에만 있는 대상 + b에만 있는 대상
print(a ^ b)



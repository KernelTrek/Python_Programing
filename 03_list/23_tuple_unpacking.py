num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 20)
print(x, y)

# 많이 쓰면 보기 싫음.
a, b, c, d, e, f = 'Mike', 1, 2, 3, 4, 5

min, max = 0, 100
print(min, max)

i = 10
j = 20

# swap 하기
tmp = i
i = j
j = tmp

print(i, j)

# 이방법도 됨 .
i, j = j, i
print(i, j)
y = [1, 2, 3]
x = 1

if x in y:
    print('in')
else:
    print('not in')

if 100 not in y:
    print('not in 2')

a = 1
b = 2

# 비추천
if not a == b:
    print('not equal')

if a != b:
    print('not equal')

is_ok = True

# 낫은 이런식으로 표기
if not is_ok:
    print('hello')
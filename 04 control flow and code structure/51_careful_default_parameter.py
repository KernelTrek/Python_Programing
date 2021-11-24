# 참조반환 되는 대상은 디폴트 인수로 생성하면 안된다.
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
test_func(100, y)
print(y)

y = [1, 2, 3]
test_func(200, y)
print(y)

# 문제점
r = test_func(100)
print(r)

r = test_func(200)
print(r)

# 좋은 변환예
def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return(l)

# generator 는 반복처리를 할때, 한 요소를 꺼내서 생성해 가면서 하는것이다
# 주로 오래걸리는 작업의 분할 처리를 해야할 경우에 사용 된다.
l = ['Good Morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("#############")

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

print("#############")
g = greeting()
print(next(g))
print(next(g))

print("#############")

# python 은 yield 를 사용하면 제너레이터라고 판단한다.
def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()

print(next(c))
print(next(c))
print(next(c))

# test
def greeting2():
    yield 'Good morning'
    for i in range(10):
        print(i)
    yield 'Good afternoon'
    for j in range(10):
        print(j)
    yield 'Good night'

g = greeting2()

print(next(g))
print(next(g))

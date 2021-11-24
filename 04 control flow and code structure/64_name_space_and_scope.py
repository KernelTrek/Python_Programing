animal = 'cat'

def f():
    # print(animal)
    # function 내에서 외부에서 사용한 적이 있는 경우 내부에서 재선언이 불가능 하다.
    animal = 'dog'
    print('after', animal)

f()
print('global:', animal)

print(globals())
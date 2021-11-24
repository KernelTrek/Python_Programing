# 값에 개수만큼 계속 추가해야함
def say_something(word, word2, word3):
    print(word)

say_something('Hi', 'Mike', 'Nance')

# 튜플화 해버린다면
def say_something2(word, *args):
    print(word)
    for arg in args:
        print(arg)

say_something2('Hi', 'Mike', 'Nance')

# 밑에 2줄은 잘 사용안하며, 위와 같이 표현을 많이함
t = ('Mike', 'Nanc')
say_something2('Hi!', *t)
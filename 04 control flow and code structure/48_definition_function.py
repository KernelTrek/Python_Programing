def say_something():
    s = 'hello'
    print('hi')
    return s

result = say_something()

print(result)

# 인수 넣기
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)


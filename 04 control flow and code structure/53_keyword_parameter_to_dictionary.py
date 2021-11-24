def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='coffe')

def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffe')

d = {
    'entree': 'beef',
    'drink': 'icecoffe',
    'dessert': 'ice'
}
menu(**d)


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

# 순서가 틀리면 에러가 뜸
menu('banana', 'apple', 'orange', entree='beef', drink='coffe')

def menu(entree, drink, desert):
    print(entree)
    print(drink)
    print(desert)

menu('beef', 'beer', 'ice')

menu(entree='beef', desert='beer', drink='ice')

# default 인수 지정
def menu2(entree='beef', drink='beer', desert='ice'):
    print(entree)
    print(drink)
    print(desert)

menu2()
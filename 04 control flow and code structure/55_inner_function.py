def outer(a, b):
    def plus(c, d):
        return c + d
    print(plus(a, b))

outer(1, 2)

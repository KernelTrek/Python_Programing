class Word(object):

    # __ __ 들어가는 대상이 특수 메서드임
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "word !!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
print(w)
print(len(w))

w2 = Word('##########')

print(w + w2)
print(w == w2)

print(id(w))
print(id(w2))

"""
__eq__
__ne__
__gt__
__le__
__ge__

__add__
__sub__
__mul__
... 등등...
"""
#잘못 작성된 요일
l = ['Mon', 'Tue', 'wed', 'Thu', 'fri', 'Sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)

# lambda 로 표현하면
sample_func2 = lambda word: word.capitalize()

change_words(l, sample_func2)
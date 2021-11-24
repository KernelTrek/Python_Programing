# 예외를 개인적으로 만들수 있음.
#raise IndexError('test error')

# Exception 의 기능을 계승 받아서 사용
class UppercaseError(Exception):
    pass

def check():
    words = ['apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

check()

def check2():
    words = ['Apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check2()
# 독자적인 에러를 발생 시킬때는, 기존의 에러를 사용하지 않는 편이 좋다.
except UppercaseError as exc:
    print(f"This is my fault. Go next {exc}")
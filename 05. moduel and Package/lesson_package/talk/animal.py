# from lesson_package.tools import utils
# 아래 방식은 비추천이나.. 프로젝트를 잘못 생성해서... 잘생성하는 경우 위의 방식 무조건 사용
from ..tools import utils

def sing():
    return '##aksjdljqwkjlekjqlkweqw'

def cry():
    return utils.say_twice('qwioeuoiqwflkajkljdas')

if __name__ == '__main__':
    print(sing())
    print(f"animal : {__name__}")
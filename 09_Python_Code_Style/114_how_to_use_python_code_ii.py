"""
임포트 하는 방법

"""

# from 에서 함수를 읽어오는 것을 하지는 말자.
# import 순서는 시스템 -> 3rd Party -> Local -> 자신만의 세팅

import os
import sys

import flask

import test
from test import aaa

# 모든 exception은 하지 않느 것이 좋다.
# 파일별로 에러 코드를 부여해서 어떤 에러가 났는지 기록할수 있도록 하자.
class MainError(Exception):
    pass

def main():
    print('test')
    raise MainError('error')

# 중첩 포문은 아래와 같이 표기하는 것은 좋지 않다.
x = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]

d = {'key1': 'value1'}

# 키를 확인할떄는 아래와 같이 확인하자.
if 'key1' in d:
    print('test')

# 좋지 않은 패턴
if 'key1' in d.keys():
    print('test')

# 변수명은 알아볼수 있는 것으로 작성해주는 것이 좋다.
for k, v in d.items():
    print(k, v)
# example
# for name, count in ranking.items():

# generator 의 경우 사용할수 있으면 사용하는 것이 좋다.
# yield 사용하는 패턴
def t():
    num = []
    for i in range(10):
        num.append(i)
    return num

for i in t(0):
    print(i)

# 람다 관련 단순 표기가 가능하다면 이렇게 표기 )
def test_func(x):
    return x * 2

lambda x : x * 2

# if 표기의 단축 표기
y = None
x = 1 if y else 2
print(x) # x = 2

# 리스트를 클래스나 함수의 defualt value로 주면 안된다.
# 반드시 생성자 내에 선언할 것

# if 문에서 굳이 빈 파일들에 대해서 = [] , == {} 로 표기하지 말자.

# 클로저 내부의 변수는 다른 사람이 덮어 쓰지 않도록 글로벌 변수를 사용하지 않는다.
def base(x):
    def plus(y):
        return x + y
    return plus

plus = base(10)
print(plus(10)) # 20
print(plus(40)) # 50


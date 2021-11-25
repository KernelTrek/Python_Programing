# from lesson_package.talk import human
# from lesson_package.talk import animal
# __init__ 에 선언된 all 기준으로 import 된다.
# 다만 추천하지는 않는 방식임.
from lesson_package.talk import *

print(human.sing())
print(human.cry())

print(animal.sing())
print(animal.cry())

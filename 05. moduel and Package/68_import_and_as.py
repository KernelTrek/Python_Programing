# 방법은 여러가지가 있다.
import lesson_package.utils
from lesson_package import utils
#from lesson_package.utils import say_twice

r = lesson_package.utils.say_twice('hello')

r2 = utils.say_twice('hello2')

print(r)
print(r2)
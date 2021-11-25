# pakage 에서 옛날 버전을 위에 넣고 밑에는 신규 버전을 넣는 등으로 하면된다.
# 보통 업데이트로 인한 사건 발생시 사용하는 편이다.
try:
    from lesson_package import docutils
except ImportError:
    from lesson_package.tools import utils

print(utils.say_twice('word'))
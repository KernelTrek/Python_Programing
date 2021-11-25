# 1. import 라이브러리는 1개씩 작성한다.
# 2. 알파벳 순으로 작성한다.
# 3. 서드 파티 라이브러리를 사용하는 경우 분리해서 아래에 넣는다.
# 4. 사용자 유저 라이브러리도 분리해서 넣는다.
# 5. 파일등을 읽어 올때도 분리해서 넣는다.
import collections
import os
import sys

# goto -> Declation
import termcolor

import lesson_package

import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)
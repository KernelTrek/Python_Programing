# ; 를 사용할수는 있지만 사용하지 않는게 좋다.
x = 1;
y = 2;

# 코드 라인은 80 개 이하가 좋다.
# perferens (setting) -> Code Style창에 수치값 조정
a = "aaqwkehjqwkhrhjkqwhhoidsahjifdafaaqwkehjqwkhrhjkqwhhoidsahjifdafaaqwkehjqwkhrhjkqwhhoidsahjifdafaaqwkehjqwkhrhjkqwhhoidsahjifdaf"
# 줄을 변경할 떄는 indent 를 맞춰주자
def test_func(x, y,
              c = "aahjkhjkrhqjkwhrjkhqjkwhduiqwydiouwqyuoieuqiowueiopquwioe"):
    """

    :param x:
    :param y:
    :param c:
    :return:

    URL 을 넣을때는 더 길어도 괜찮다.
    See details at :
    """
    print('test')

# 필요없는 괄호는 사용하지 말자.
if (x and y):
    print('exist')

    x = {'test': 'sss'}


# Python의 기본 indent 는 스페이스 4개 이다.
# Code Style -> Python -> Tab : 4 로 설정


# 값을 입력할때는, 는 항상 바로 뒤에 넣는다.
x, y = y, x
x = {'test': 'xxx'}
# def test2(a, b, c):

# 연산자 데이터를 넣을떄는 이렇게 해라
a = 10 + 20

# = 의 라인을 맞출 필요는 없다. 변수명이 길면 다바꿀 것인가 ?


# 클래스 정의 간의 간격은 2줄을 만들고/ 함수 와의 간격에는 1줄로 나열한다.
# 글로벌 정의의 경우에도 모두 2줄을 뛰우자 import 후 2줄 , 글로벌 변수 선언후 2줄


word = 'hello'
word2 = '!'

# 단순 문자열 연결에서는 + 로 나열하는 것이 좀더 깔끔하다.
new_word = word + word2

# 문자열을 길게 하려면 아래와 같이 사용하는 방식은 추천하지 않는다. [비추천]
long_word = ""
for word in {'aasdas', 'asdqwdqw', 'wqrqwrqw'}:
    long_word += "{}asdasd".format(word)

# 리스트를 활용해서 추천하는 방식을 추천함. [ 추천]
long_word = []
for word in {'aasdas', 'asdqwdqw', 'wqrqwrqw'}:
    long_word.append("{}asdasd".format(word))
new_log_word = ''.join(long_word)

# 문자를 표기할떄 ' 와 " 를 구별하는 경우 둘다 구별하는 것이 좋다.
# 회사마다 다르나, ' 는 단어, " 는 문장을 나타내는 경우가 있고.
# 보통은 ' 만 사용하고, 문장내 싱글쿼트 (') 가 나오는 경우 " 를 사용하는 경우도 있다.
print('asdas')
print("asdas")


# 파일을 열거나 특정 open을 할때는 별다른 사유가 없다면, with 로 사용하는 것이 좋다.
# 내가 미래에 할 작업의 관해서는 아래와 같이 달아 주는 것이 좋다.
# TODO (jaehyeonlee) Use locking machine for avoiding dead lock issue
with open('file.txt', 'w') as file:
    print('test')


# if 문은 한줄로 표기가 가능하나, 회사 분위기에 따라 다른편이다.
if x:
    print('exit')
else:
    print('else')
if x: print('exit')
else: print('else')

# 변수명 작성 방법
# class 의 경우 Camel Case 를 활용한다. Apple
# 변수와 함수명의 경우 모두 소문자를 사용하고, _로 연결해주자
# Global 변수의 경우 대문자로 작성한다.

"""
 main 문에서는
 def main():
    main 문 작성
    
 if __name__ == '__main__':
    main()
    
"""
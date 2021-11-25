# 클래스가 생성될떄 사용하는것 / 종료될떄 하는것.
class Person(object):
    # 생성자
    # initialise 초기화 (이름을 받아서 초기화 하기 )
    def __init__(self, name = "Defualt Name"):
        self.name = name
        print(self.name)

    # self 를 붙이지 않으면 내부 변수나 자기 자신을 사용할수 없다.
    def say_something(self):
        print(f"I am {self.name}. Hello~!")
        self.run(3)

    def run(self, num):
        print('run' * num)

    # 종료 될때 호출됨
    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

del person

print('##########')


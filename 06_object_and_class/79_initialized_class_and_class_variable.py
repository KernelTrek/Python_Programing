class Person(object):
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

person = Person('Mike')
person.say_something()
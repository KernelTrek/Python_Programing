class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    # class method 는 object 로 생성되지 않고, 클래스의 메소드로 선언되어 사용가능함
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    # 쓸일은 많이 없을수 있음. 
    @staticmethod
    def about(year):
        print(f"about human {year}")

a = Person()
print(a.x)
b = Person
# 실행 불가 초기화 이후 (객체 생성 이후) 생성
#print(b.x)
# 실행 가능
print(b.kind)
print(Person.kind)
print(Person.what_is_your_kind())

Person.about(1999)
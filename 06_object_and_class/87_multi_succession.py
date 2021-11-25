class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('run')

# 계승 순서에 따라, 이미 정의된 대상을 먼저 가져오고 중복되면 상속받지 않을 수도 있다.
class PersonCarRobor(Car, Person):
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobor()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()
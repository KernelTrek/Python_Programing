# class 선언후 pass 만 넣으면, 아무 기능을 하지 않는다는 의미로 넣는다.
class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def autorun(self):
        print('autorun')

car = Car()
car.run()

# 없지만 상속을 받아서 실행이 된다.
toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.autorun()
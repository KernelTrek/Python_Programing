class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model="Model S", enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run
    def run(self):
        print('superfast')
    def autorun(self):
        print('autorun')

car = Car()
print(car.model)
car.run()
print("##########################")
# 없지만 상속을 받아서 실행이 된다.
toyota_car = ToyotaCar('Lexus')
toyota_car.run()
print(toyota_car.model)
print("##########################")
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.autorun()
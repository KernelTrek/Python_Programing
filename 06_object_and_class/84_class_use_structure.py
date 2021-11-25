class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model="Model S", enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    # 밖에서 해당 변수를 수정하지 못하게 하려고 아래와 같이 변경함
    #property Getter
    @property
    def enable_auto_run(self):
        return  self._enable_auto_run

    # property Setter : 설정하지 상단에 겟터가 있는 경우 값 변경이 불가능함
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('superfast')

    def autorun(self):
        print('autorun')

class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)
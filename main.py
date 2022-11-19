#import 패키지명.모듈명
import pizza_factory.factory as f
import pizza_factory.pizza as p
from pizza_factory.factory import *
from pizza_factory.pizza import *
import pizza_factory.pizza
import pizza_factory.factory

# 패키지.모듈.함수 접근
pizza_factory.pizza.make_pizza("페퍼로니")
pizza_factory.factory.run_factory()

#from 패키지.모듈 import 함수, 변수

make_pizza("치즈")
run_factory()

# 별명 이용

p.make_pizza("치즈")
f.run_factory()



class Person:
    def __init__(self):
        self.name = input('이름: ')
        self.age = int(input('나이: '))

    def disp(self):
        print(self.name + ':' + str(self.age))


li = []
for i in range(3):
    li.append(Person())
for i in li:
    i.disp()



class Sj:
    def __init__(self):
        self.kor = 90
        self.__eng = 77                                      # 접근제한자, __를 붙이면 접근할수 없다. AttributeError: 'Sj' object has no attribute 'eng'
    #def disp(self):                                         # 접근제한이 걸려있어도, 같은 클래스 내의 함수를 정의해서(메소드) 접근 가능하다.
    #    print(self.__eng)
    def geteng(self):                                        # 일반적으로 값을 불러올 때 get을 쓴다.
        return self.__eng
    def seteng(self, eng):                                   # 값을 넣을 때 set을 쓴다.
        self.__eng = eng


s1 = Sj()
#print(s1.__eng)                                             # 에러
#s1.disp()
print(s1.geteng()) 
s1.seteng(100)
print(s1.geteng())

class Unit:                  
    def __init__(self):
        self.life = 50
        self.speed = 10
        self.power = 10
        self.defense = 1
        # print(type(self))    

    def move(self):
        print("움직입니다.")

class GroundUnit(Unit):    
    def __init__(self):
        super().__init__()                                  # super는 부모클래스를 나타낸다. 상속받을 떄 부모 클래스를 다시한번(?)초기화 하고 자신만의 속성을 선언한다. 해당코드가 없으면 자식 클래스의 초기화 함수에선 새로 선언한 속성에 접근 가능하지만, 자식 클래스 내의 다른 메소드에선 해당 속성에 접근이 불가능 하다.
        self.new = "new"
    def show_stats(self):
        print(self.life)
        print(self.power)
        print(self.speed)
        print(self.defense)
        print(self.new)

ground_unit = GroundUnit()
# print(ground_unit.new)
ground_unit.show_stats()

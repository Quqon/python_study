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

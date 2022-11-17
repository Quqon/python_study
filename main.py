#import 패키지명.모듈명
import pizza_factory.pizza
import pizza_factory.factory

#패키지.모듈.함수 접근
pizza_factory.pizza.make_pizza("페퍼로니")
pizza_factory.factory.run_factory()

#from 패키지.모듈 import 함수, 변수
from pizza_factory.pizza import *
from pizza_factory.factory import *

make_pizza("치즈")
run_factory()

#별명 이용
import pizza_factory.pizza as p
import pizza_factory.factory as f

p.make_pizza("치즈")
f.run_factory()
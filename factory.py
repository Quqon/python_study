#import 파일명(모듈명)
# import pizza
# pizza.make_pizza("페퍼로니")
# pizza.make_pizza_box("페퍼로니")

#form 모듈 import 함수, 변수, 클래스
#from pizza import make_pizza_box      #특정 리소스에만 접근할 수 있다. 모듈명을 붙이지 않아 편리할 수 있지만, 코드가 길어질수록 원래 선언된 위치를 찾기 어려울 수 있다.
#make_pizza_box("포테이토")

#from 모듈 import *                     #불러온 모듈의 모든 리소스에 접근 가능.
# from pizza import *
# make_pizza("포테이토")
# make_pizza_box("포테이토")

#import 모듈 as 별명                     #불러온 모듈을 원하는대로 이름지어 사용 가능. 과하게 축약하면 알아보기 힘드므로 주의해야 함.
# import pizza as p
# p.make_pizza_box("포테이토")

#from 모듈 import 함수 as 별명 1, 변수 as 별명 2, 클래스 as 별명 3
from pizza import make_pizza as mp, make_pizza_box as mpb
mp("치즈")
mpb("치즈")
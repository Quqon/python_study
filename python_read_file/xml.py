#XML 파일 만들기
from xml.etree.ElementTree import *

person=Element('Person')
name=Element('name')
name.text='홍길동'
person.append(name)
age=Element('age')
age.text='15'
person.append(age)
SubElement(person, 'adress').text='대구'            #위의 코드를 한줄로 만드는 방식
dump(person)                                        #최종적으로 만든 것을 표현하겠다라는 느낌.(=dump)
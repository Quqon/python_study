class Unit:                  #unit들이 공통적으로 사용하는 속성들과 함수들
    def __init__(self):
        self.life = 50
        self.speed = 10
        self.power = 10
        self.defense = 1
        print(type(self))    #자식클래스가 객체화 될때 자식클래스의 타입을 알려줌. 또는 자신의 클래스 타입을 알려 줌.

    def move(self):
        print("움직입니다.")

class GroundUnit(Unit):      #GroundUnit(자식클래스)에 Unit(부모클래스)을 상속. 지상유닛 클래스
    def show_stats(self):
        print(self.life)
        print(self.power)
        print(self.speed)
        print(self.defense)
        print(type(self))    #Unit이 GroundUnit에 상속되어서 __main__.GroundUnit으로 타입이 찍힘.

class AirUnit(Unit):         #공중 유닛 클래스
    def move(self):
        print("공중 유닛이 움직입니다.")

    def fly(self):
        self.move()
        #print(type(self))

# unit = Unit()              #하나만 상속했을 땐 자식클래스 이름이 나왔지만, 여러개 상속하면 상속하지 않고 type을 찍은것과 같이 __main__.Unit으로 나옴.
# unit.move()

#ground_unit = GroundUnit()
#ground_unit.show_stats()    #부모클래스에 속성(변수)가 있으므로 사용 가능.
#ground_unit.move()          #부모클래스에 정의된 함수를 사용 가능.

air_unit = AirUnit()
air_unit.fly()


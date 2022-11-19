class Point:
    def __init__(self):
        self.x = int(input('x = '))
        self.y = int(input('y = '))
    def disp(self):                                             #자식 클래스에서 사용할 것이기 때문에 pass로 넘김.
        pass
class Rect(Point):
    def __init__(self):
        super().__init__()
        self.w = int(input('w = '))
        self.h = int(input('h = '))
    def disp(self):
        print('사각형', self.x, self.y, self.w, self.h)
class Circle(Point):
    def __init__(self):
        super().__init__()
        self.r = int(input('r = '))
    def disp(self):
        print('원', self.x, self.y, self.r)
def main():
    li = list()
    while True:
        s = input('1.사각형 2.원 3.조회 4.종료: ')
        if s == '1':
            li.append(Rect())
        if s == '2':
            li.append(Circle())
        if s == '3':
            for i in li:
                i.disp()
        if s == '4':
            print('프로그램을 종료 합니다.')
            break
        if s == '5':
            print(li)                                           #[<__main__.Rect object at 0x10122fc70>, <__main__.Circle object at 0x10122fc10>] 이렇게 list안에 추가되어있는 것을 확인할수 있다. 따라서 3.조회를 했을때 각자 자식 클래스의 disp()메소드가 실행 되는 것.

main()
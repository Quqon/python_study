class Robot:
    robot_total_count = 0

    def __init__(self, name):
        print("{} 객체가 만들어집니다." .format(name))
        self.name = name
        Robot.robot_total_count += 1
        print("현재까지 생선된 로봇의 수: {}".format(Robot.robot_total_count))

    def print_name(self):
        print("제 이름은 {} 입니다.".format(self.name))

    def move(self, direction):
        print("{} 쪽으로 움직입니다.".format(direction))

    def move_left(self):
        self.move("left")

    @staticmethod
    def fly():
        print("날아갑니다")


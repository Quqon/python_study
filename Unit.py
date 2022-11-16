class Unit:
    def __init__(self):
        self.life = 50
        self.speed = 10
        self.power = 10
        self.defense = 1

    def move(self):
        print("움직입니다.")

class GroundUnit(Unit):
    def show_stats(self):
        print(self.life)

ground_unit = GroundUnit()
ground_unit.show_stats()
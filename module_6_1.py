import random

# Класс Animal описывает общее поведение животных
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed

        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        return print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("...")

# Класс Bird описывает птиц и наследуется от Animal
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

# Класс AquaticAnimal описывает плавающих животных и наследуется от Animal
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # Берем модуль dz
        self._cords[2] = self._cords[2] - dz * (self.speed / 2)

# Класс PoisonousAnimal описывает ядовитых животных и наследуется от Animal
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

# Класс Duckbill описывает утконоса и наследуется от всех трех классов: Bird, AquaticAnimal и PoisonousAnimal
class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

if __name__ == "__main__":
    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()
    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()
    db.lay_eggs()
    print(Duckbill.mro())
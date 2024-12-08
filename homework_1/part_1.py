class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} говорит: {self.sound}")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Гав-Гав")
        self.color = color

    def makesound(self):
        print(f"{self.name} говорит: {self.sound} (цвет животного:{self.color})")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Мур-Мяу")
        self.color = color

    def makesound(self):
        print(f"{self.name} говорит: {self.sound} (цвет животного:{self.color})")

my_dog = Dog(name="Бобик", color="Чёрный")
my_cat = Cat(name="Муся", color="Серый")

my_dog.makesound()
my_cat.makesound()
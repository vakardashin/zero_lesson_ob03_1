#
#
# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating")

# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} chirps")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} roars")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} hisses")

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс для сотрудников ZooKeeper и Veterinarian
class ZooKeeper:
    def feed_animal(self, animal):
        print(f"ZooKeeper is feeding {animal.name}")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Veterinarian is healing {animal.name}")

# Класс Zoo с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

# Пример использования созданных классов
bird = Bird("Sparrow", 3)
mammal = Mammal("Lion", 5)
reptile = Reptile("Snake", 2)

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

zookeeper.feed_animal(bird)
veterinarian.heal_animal(mammal)


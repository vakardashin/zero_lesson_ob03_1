# Зоопарк
#
# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает")


# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чик чирик")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рычит")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит")


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Класс для сотрудников ZooKeeper и Veterinarian
class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Сотрудник кормит {animal.name}")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")


# Класс Zoo с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} поселено в зоопарк")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} принят в зоопарк")


# Пример использования созданных классов
bird1 = Bird("Птица", 3)
mammal1 = Mammal("Лев", 5)
reptile1 = Reptile("Питон", 2)

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

zoo = Zoo()  # Объект Зоопарк
zoo.add_animal(bird1)  # Заселяем новую птицу
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)
zoo.add_staff(zookeeper)  # Принимаем нового сотрудника
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

zookeeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)


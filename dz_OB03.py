class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} кушает")

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Тру-ля-ля")

class Mammal(Animal):
    def make_sound(self):
        print("Ррррр!")

class Reptile(Animal):
    def make_sound(self):
        print ("Шшшшшш!!!")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} добавлен в зоопарк")


class Zookeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник кормит животное {animal.name}")

class Vet():
    def heal_animal(self, animal):
        print(f"Ветеринар лечит животное {animal.name}")

bird1 = Bird("Попугай", 2)
mammal1 = Mammal("Шимпанзе", 10)
reptile1 = Reptile("Кобра", 1)


zoo = Zoo()
keeper = Zookeeper()
vet = Vet()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(vet)

animal_sound(zoo.animals)

keeper.feed_animal(bird1)
vet.heal_animal(reptile1)

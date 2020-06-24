class Animal:
    type = "В классе не определен тип животного (корова, овца, коза и т.д.)"  # вид животного
    voice = "В классе не определен звук, который издает животное (мычание, кукарекание и т.д.)"  # звук животного

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"Кормление животного: {self.type} '{self.name}'")

    def voice_say(self):
        print(f"{self.type} {self.name} издает звук '{self.voice}'")

class Cow(Animal):
    type = "корова"
    voice = "му-у"

    def milk(self):
        print(f"Доить: {self.type} '{self.name}'")

class Goat(Cow):
    type = "коза"
    voice = "ме-е"

class Sheep(Animal):
    type = "овца"
    voice = "бе-е"
    def shear(self):
        print(f"Стрижка: {self.type} {self.name}")

class Birds(Animal):
    def egg_collect(self):
        print(f"Собрать яйца у: {self.type} '{self.name}'")

class Chicken(Birds):
    type = "курица"
    voice = "ко-ко"

class Duck(Birds):
    type = "утка"
    voice = "кря-кря"

class Goose(Birds):
    type = "гусь"
    voice = "га-га"

goose1 = Goose("Серый", 5)
goose2 = Goose("Белый", 8)
cow = Cow("Манька", 500)
sheep1 = Sheep("Барашек", 100)
sheep2 = Sheep("Кудрявый", 90)
chicken1 = Chicken("Ко-Ко", 1)
chicken2 = Chicken("Кукареку", 1.2)
goat1 = Goat("Рога", 55)
goat2 = Goat("Копыта", 60)
duck = Duck("Кряква", 3)

animals = [goose1, goose2, cow, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck]
for animal in animals:
    animal.feed()

for cattle in [cow, goat1, goat2]:
    cattle.milk()

for sheep in [sheep1, sheep2]:
    sheep.shear()

for bird in [goose1, goose2, chicken1, chicken2, duck]:
    bird.egg_collect()

for animal in animals:
    animal.voice_say()

animal_max_weight = 0
animal_name = 0
for animal in animals:
    if animal.weight > animal_max_weight:
        animal_max_weight = animal.weight
        animal_name = animal

print(f"Максимальный вес {animal_max_weight} кг у животного: {animal_name.type} '{animal_name.name}'")
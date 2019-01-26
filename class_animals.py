# Домашнее задание к лекции «Классы и их применение в Python»
class Animal:
    total_weight = 0
    heaviest_animal = None

    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice
        Animal.total_weight = 0
        Animal.heaviest_animal = None

    # Описываем общие методы взаимодействия: кормление, голос, продукт
    def feed(self):
        # Животные на ферме, которых нужно кормить
        print("  {}".format(self.name))

    def voice(self):
        # различать по голосам
        print(' {} {}'.format(self.name, self.voice))

    def product(self):
        # Продукт, который получает дядюшка от животных на ферме от стрижки, дойки, сбора яиц
        pass


# Класс для овец
class Sheep(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'бе-бе-бе')

    # Метод shear(стрич)
    def shear(self):
        # овец стричь(shear)
        print("  шерсть от {}".format(self.name))

    # Переопределение метода для вызова метода shear
    def product(self):
        self.shear()


# Общий класс для коров и коз, в которм будет создан метод milk
# Класс является потомком Animal: наследуются параметры, методы(feed, voice)
class MilkAnimal(Animal):
    def milk(self):
        # корову и коз доить
        print("  молоко от {}".format(self.name))

    def product(self):
        self.milk()


# Классы для коров и коз. Наследуем методы от родителя MilkAnimal и Animal
class Cow(MilkAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'мууу')


class Goat(MilkAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'ме-ме-ме')


# Общий класс для птиц.
# Класс является потомком Animal. Наследуются параметры, методы(feed, voice)
# Добавлен метод - egg и переопределен метод product для запуска egg
class Bird(Animal):
    def egg(self):
        # собирать яйца у кур, уток и гусей
        print("  яйца от {}".format(self.name))

    def product(self):
        self.egg()


# Классы для гусей, кур и уток. Наследуем методы от родителя Bird и Animal
class Goose(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'га-га-га')


class Chicken(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'кудахчет')


class Duck(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'кря-кря-кря')


# Для каждого животного из списка должен существовать экземпляр класса.
goose1 = Goose('Гусь "Серый"', 4.2)
goose2 = Goose('Гусь "Белый"', 3)
cow = Cow('Корова "Манька"', 100.37)
sheep1 = Sheep('Овечка "Барашек"', 25.4)
sheep2 = Sheep('Овечка "Кудрявая"', 28.3)
goat1 = Goat('Коза "Рога"', 25.4)
goat2 = Goat('Коза "Копыта"', 28.7)
chicken1 = Chicken('Курица "Ko-Ko"', 2.5)
chicken2 = Chicken('Курица "Кукареку"', 3.2)
duck = Duck('Утка "Кряква"', 4.5)

animals = [goose1, goose2, cow, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck]

print('\nЖивотные на ферме, которых нужно кормить:')
for animal in animals:
    animal.feed()

# Вывести животных, которых соответственно требуется подоить/постричь/собрать яйца
print('\nПродукт, который получаем от животных на ферме:')
for animal in animals:
    animal.product()

print('\nРазличать по голосам: ')
for animal in animals:
    # animal.voice()
    print('  {} - {}'.format(animal.name, animal.voice))

for animal in animals:
    Animal.total_weight = Animal.total_weight + animal.weight
print('\nОбщий вес всех животных: {} '. format(Animal.total_weight))

for animal in animals:
    if Animal.heaviest_animal is None:
        Animal.heaviest_animal = animal
    elif animal.weight > Animal.heaviest_animal.weight:
        Animal.heaviest_animal = animal
print('Самое тяжёлое животное: {}, имеет вес: {} кг, издаёт звук: {} '.format(Animal.heaviest_animal.name,
                                                                              Animal.heaviest_animal.weight,
                                                                              Animal.heaviest_animal.voice))


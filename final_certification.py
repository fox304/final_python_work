import logging

FORMAT = '{levelname:<18} - {asctime}.\n В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()\n" ' \
         'в {created} секунд записала сообщение:\n {msg}\n'
logging.basicConfig(filename="logs.log",
                    filemode="w",
                    encoding="utf-8",
                    format=FORMAT,
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Animal:
    def __init__(self,name):
        logger.info(f"содано животное  {name}")
        self.name = name


class Bird(Animal):
    def __init__(self,name,wingspan):
        super().__init__(name)
        self.wingspan = int(wingspan)

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self,name,max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        category = "Мелководная рыба" if self.max_depth < 10 else \
            "Глубоководная рыба" if self.max_depth > 100 else "Средневодная рыба"
        return category


class Mammal(Animal):
    def __init__(self,name,weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        category = "Малявка" if self.weight < 1 else \
            "Гигант" if self.weight > 200 else "Обычный"
        return category


class AnimalFactory:

    @staticmethod
    def create_animal(animal_type,*args):
        list_types_animals = ('Bird','Fish','Mammal')
        if animal_type not in list_types_animals:
            logger.error(f"Такие виды животных как {animal_type} здесь не водятся")
            raise ValueError("Недопустимый тип животного")
        new_instance = Bird(*args) if animal_type == list_types_animals[0] else \
            Fish(*args) if animal_type == list_types_animals[1] else \
                Mammal(*args)
        return new_instance


# Создание экземпляров животных
animal1 = AnimalFactory.create_animal('Bird','Орел',200)
animal2 = AnimalFactory.create_animal('Fish','Лосось',50)
animal3 = AnimalFactory.create_animal('Mammal','Слон',5000)

# Вывод результатов
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())

#

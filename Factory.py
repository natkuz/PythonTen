# 📌Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# Доработайте задачу
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

# Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from random import choice

class Factory:
    ears_list = ['big round ears', 'little round ears', 'big triangle ears', 'little tryangle ears', 'ears like hairs']
    wool_list = ['curly wool', 'long smooth wool', 'shaggy wool', 'fluffy wool']
    wool_color_list = ['red', 'grey', 'striped', 'spotted', 'black']
    eyes_list = ['green eyes', 'orange eyes', 'yellow eyes', 'brown eyes', 'black eyes']
    paws_list = ['soft paws', 'clawed paws', 'hooves']
    tails_list = ['striped tail', 'long tail', 'short tail', 'ring tail']

    def __init__(self, type_animal: str, name: str, age: int, special: str = None):
        self.type_animal = type_animal
        self._name = name
        self._age = age
        self._special = special

    def new_animal(self):
        self._ears = choice(self.ears_list)
        self._wool = choice(self.wool_list)
        self._wool_color = choice(self.wool_color_list)
        self._eye = choice(self.eyes_list)
        self._paw = choice(self.paws_list)
        self._tail = choice(self.tails_list)
        self.n_animal = [self.type_animal, 'name ' + self._name, 'age ' + str(self._age) + ' year(s)',
                         self._ears, self._wool_color + ' ' + self._wool, self._eye, self._paw, self._tail,
                         "just lucky" if self._special is None else self._special]
        return self.n_animal


class Animal:

    def __init__(self, name: str, age: int, special: str):
        self._name = name
        self._age = age
        self._special = special

    def get_special(self):
        return self._special


class Dog(Animal):

    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('breed', None))


class Cat(Animal):

    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('color', None))


class Fish(Animal):

    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('habitat', None))


# spanky = Dog('Spanky', 3, breed='spaniel')
# tom = Cat('Tom', 15, color='blue')
# dory = Fish('Dory', 4, habitat='home')
#
# for animal in [spanky, tom, dory]:
#     print(animal.get_special())

an = Factory('cat', 'Lapa', 1)
print(an.new_animal())
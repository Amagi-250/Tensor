print('---------')
print('Задание 1')
print('---------')

class Animals:
    def __init__(self, weight, color, make_sound):  # конструктор
        self.weight = weight
        self.color = color
        self.make_sound = make_sound

    def speak(self):
        print('Вы вызвали класс "Animals"')

Anim = Animals('0-10000', 'RGB', 'GOLOS')
Anim.speak()

class Mammals(Animals):
    def __init__(self, weight, color, make_sound, wool, milk_feeding):  # конструктор
        super().__init__(weight, color, make_sound)
        self.wool = wool
        self.milk_feeding = milk_feeding

    def info(self):
        print('\nКласс "Mammals" отличается от остальных тем, что у '
              'животных данного типа есть волосянной покров и они кормят '
              'своих детёнышей своим молоком')

Mammal = Mammals('0-10000', 'RGB', 'GOLOS', 'boolean', 'boolean' )
Mammal.info()

class Human(Mammals):
    def __init__(self, gender, name, age, weight, color, make_sound, wool, milk_feeding, height, passport ):  # конструктор
        super().__init__(weight, color, make_sound, wool, milk_feeding)
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.passport = passport

    def say(self, text):
        print(f'{self.name} говорит: {text}')

Ilya = Human('Мужской', 'Илья', 20, 73, 'Розовый', 'Привет!', 'Да', 'Нет', 178, '23_31_314143')
print(f"\n{Ilya.make_sound}")
Ilya.say('\nПривет, мне зовут Илья, мне 20 лет')
print(f"Пол: {Ilya.gender}")
print(f"Рост: {Ilya.height} см")
print(f"Вес: {Ilya.weight} кг")
print(f"Серия и номер паспорта: {Ilya.passport}")

class Cat(Mammals):
    def __init__(self, name, age, weight, color, wool, milk_feeding, make_sound, ears):  # конструктор
        super().__init__(weight, color, make_sound, wool, milk_feeding)
        self.name = name
        self.age = age
        self.ears = ears

    def make_soun(self):
        print('\nMeow')

Musya = Cat('Муся', 3, 10, 'Трёхцветный', 'Да', 'Да', 'Мяу', 'Острая')
Musya.make_soun()
print(f"Меня зовут: {Musya.name}")
print(f"Мне: {Musya.age} года")
print(f"Вес: {Musya.weight} кг")
print(f"Цвет шерсти: {Musya.color}")
print(f"Форма ушей: {Musya.ears}")

class Dog(Mammals):
    def __init__(self, name, age, weight, color, wool, milk_feeding, make_sound, ears):  # конструктор
        super().__init__(weight, color, make_sound, wool, milk_feeding)
        self.name = name
        self.age = age
        self.ears = ears

    def info(self):
        print(f'\nЯ собака. Меня зовут {self.name}. Мне {self.age} лет.')

Grey = Dog('Грей', 7, 23, 'Чёрный', 'Да', 'Нет', 'Гав', 'Скруглённые')
print(f"{Grey.make_sound}")
Grey.info()
print(f"Вес: {Grey.weight} кг")
print(f"Цвет шерсти: {Grey.color}")
print(f"Форма ушей: {Grey.ears}")

print('\n-------------')
print('Задание 2 - 3')
print('-------------')

class Student(Human):
    def __init__(self, gender, name, age, weight, color, make_sound, wool, milk_feeding, height, passport, study, kol_dz):  # конструктор
        super().__init__(gender, name, age, weight, color, make_sound, wool, milk_feeding, height, passport)
        self.study = study
        self.kol_dz = kol_dz

    def __eq__(self, other):
        return self_com == other_com

    def __gt__(self, other):
        return self_com > other_com

    def __lt__(self, other):
        return self_com < other_com

    def __ge__(self, other):
        return self_com >= other_com

    def __le__(self, other):
        return self_com <= other_com

    def __eq__(self, other):
        return self_com != other_com

Ylyana = Student('Женский', 'Ульяна', 20, 55, 'Розовый', 'Привет', 'Да', 'Да', 165, '23_31_315232', 'Ученик', 3)
Elisey = Student('Мужской', 'Елисей', 20, 65, 'Розовый', 'Привет', 'Да', 'Да', 170, '53_74_725435', 'Ученик', 6)
Dima = Student('Мужской', 'Дмитрий', 21, 83, 'Розовый', 'Привет', 'Да', 'Да', 183, '72_23_834522', 'Ученик', 7)
Anna = Student('Женский', 'Анна', 20, 59, 'Розовый', 'Привет', 'Да', 'Да', 173, '41_43_834522', 'Ученик', 2)
Vlad = Student('Мужской', 'Владислав', 21, 76, 'Розовый', 'Привет', 'Да', 'Да', 177, '23_31_763223', 'Ученик', 6)

print(f"Количество сданных работ у Ульяны равно количеству сданных работ у Ани: {Ylyana.kol_dz==Anna.kol_dz}")
print(f"У Ульяны количество сданных работ меньше, чем у Ани: {Ylyana.kol_dz<Anna.kol_dz}")
print(f"У Ульяны количество сданных работ больше, чем у Ани: {Ylyana.kol_dz>Anna.kol_dz}")
print(f"У Ульяны количество сданных работ больше или равно, чем у Ани: {Ylyana.kol_dz>=Anna.kol_dz}")
print(f"У Ульяны количество сданных работ меньше или равно, чем у Ани: {Ylyana.kol_dz<=Anna.kol_dz}")
print(f"Количество сданных работ у Ульяны НЕ равно количеству сданных работ у Ани: {Ylyana.kol_dz!=Anna.kol_dz}")
import json
import pickle
class User:
# Создаем конструктор класса User
    def _init_(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.age = None
# Вводим исходные данные пользователя
    def input_fio(self):
        self.first_name = input("Input First Name: ")
        self.middle_name = input("Input Middle Name: ")
        self.last_name = input("Input Last Name: ")
    def input_age(self):
        self.age = input("Input Age: ")
# Создаем удобную для вывода на экран строку пользователя
    def serialize(self):
        return "First name: {}\n" \
               "Middle name: {}\n"\
               "Last name: {}\n" \
               "Age : {}\n"\
            .format(self.first_name, self.middle_name, self.last_name, self.age)
# Сохраняем данные в файл с помощью json
    def fail_save(self):
        fil = str(input("Введите с клавиатуры имя файла для записи в файл:  "))
        jdata = json.dumps((self.first_name, self.middle_name, self.last_name, self.age))
        with open(fil, "w") as f:
            f.write(jdata)
# Загружаем с файла данные для работы
    def fail_load(self):
        fil = str(input("Введите с клавиатуры имя файла для загрузки с файла:  "))
        with open(fil, "r") as f:
            d = f.read()
            p = json.loads(d)
        print(type(p))
        print(p)
# Создаем дочерний класс MaxUser
class MaxUser(User):
    # Наследование класса User с расширением функций в дочернем классе MaxUser
    def _init_(self):
        super().__init__()
        self.gender = None
    def input_fio(self):
        super().input_fio()
        self.gender = input("Input gender:")

    def serialize(self):
        res = super().serialize()
        return res + "Gender: {}\n" \
            .format(self.gender)

    # Запись данных с помощью pickle (наследование класса User с изменением поведения в дочернем классе MaxUser)
    def fail_save(self):
        fil = str(input("Введите с клавиатуры имя файла для сохранения данных:  "))
        pickle_dumps_d = pickle.dumps((self.first_name, self.middle_name, self.last_name, self.age, self.gender))
        with open(fil, 'wb') as f:
            f.write(pickle_dumps_d)
        print(pickle_dumps_d)
user = MaxUser()
user.input_fio()
user.input_age()
print(user.serialize())
user.fail_save()

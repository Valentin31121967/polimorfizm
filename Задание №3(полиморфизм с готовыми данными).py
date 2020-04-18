import json
# Создаем класс Avto
class Avto:
    # Функция конструктор класса Avto
    def _init_(self):
        self.make = None
        self.model = None
        self.year = None
        self.capacity = None
        self.mass = None
        self.colour = None
        Avto._init_()
        Man.__init__()
    # Функция ввода данных автомобиля
    def input_info_Avto(self):
        self.make = "Sckoda"
        self.model = "Fabia"
        self.year = "2010"
        self.capacity = "1,4"
        self.mass = "1756"
        self.colour = "white"
    # Функция сериализации данных в удобный вид для чтения на экране
    def serialize(self):
        return "марка: {}\n" \
               "модель: {}\n"\
               "год выпуска: {}\n" \
               "объём двигателя : {}\n"\
               "масса : {}\n"\
               "цвет : {}\n"\
            .format(self.make, self.model, self.year, self.capacity, self.mass, self.colour)
    # Функция записи данных  в отдельный файл (например 1.txt)
    def fail_save(self):
        fil = str(input("Введите с клавиатуры имя файла для сохранения данных:  "))
        with open(fil, "w") as f:
            data = {"марка": self.make,
                    "модель": self.model,
                    "год выпуска": self.year,
                    "объём двигателя": self.capacity,
                    "масса": self.mass,
                    "цвет": self.colour}
            json.dump(data, f)
        print(data)
    # Функция загрузки данных  из отдельного файла
    def fail_load(self):
        fil = str(input("Введите с клавиатуры имя файла для загрузки данных:  "))
        with open(fil, "r") as f:
            data = json.loads(f.read())
            self.make = data["марка"]
            self.model = data["модель"]
            self.year = data["год выпуска"]
            self.capacity = data["объём двигателя"]
            self.mass = data["масса"]
            self.colour = data["цвет"]
            print(data)

# Создаем новый класс Man
class Man:
    # Функция конструктор класса Man
    def _init_(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.age = None
        self.gender = None
        self.nationality = None
    # Функция ввода данных пользователя
    def input_info_Man(self):
        self.first_name = "Долматов"
        self.middle_name = "Петр"
        self.last_name = "Сергеевич"
        self.age = "50"
        self.gender = "муж"
        self.nationality = "украинец"
    # Функция сериализации данных в удобный вид для чтения на экране
    def serialize(self):
        return "Фамилия: {}\n" \
               "Имя: {}\n"\
               "Отчество: {}\n" \
               "Возраст : {}\n"\
               "Пол : {}\n"\
               "Национальность : {}\n"\
            .format(self.first_name, self.middle_name, self.last_name, self.age, self.gender, self.nationality)
    # Функция записи данных  в отдельный файл (например 1.txt)
    def fail_save(self):
        fil = str(input("Введите с клавиатуры имя файла для сохранения данных:  "))
        with open(fil, "w") as f:
            data = {"Фамилия": self.first_name,
                    "Имя": self.middle_name,
                    "Отчество": self.last_name,
                    "Возраст": self.age,
                    "Пол": self.gender,
                    "Национальность": self.nationality}
            json.dump(data, f)
    # Функция загрузки данных  из отдельного файла
    def fail_load(self):
        fil = str(input("Введите с клавиатуры имя файла для загрузки данных:  "))
        with open(fil, "r") as f:
            data = json.loads(f.read())
            self.first_name = data["Фамилия"]
            self.last_name = data["Имя"]
            self.middle_name = data["Отчество"]
            self.age = data["Возраст"]
            self.gender = data["Пол"]
            self.nationality = data["Национальность"]
            print(data)

# Создаём дочерний класс Tehpassport
class Tehpassport(Avto, Man):
    # Функция конструктор дочернего класса Tehpassport
    def __init__(self):
        Avto.__init__(self)
        Man.__init__(self)
        self.number_reg = None
        self.addres = None
        self.data_reg = None
        self.number_drive = None
    # Функция ввода данных дочернего класса Tehpassport
    def input_info_Tehpassport(self):
        super().input_info_Avto()
        super().input_info_Man()
        self.number_reg = "FDR12345"
        self.addres = "г. Харьков, проспект Льва Ландау, д.87, кв.234"
        self.data_reg = "12.05.2010"
        self.number_drive = "AX2345BM"
    # Функция сериализации удобного вывода на экран необходимых данных для дочернего класса Tehpassport
    def serialize(self):
        return "Фамилия: {}\n" \
              "Имя: {}\n" \
              "Отчество: {}\n" \
              "Марка : {}\n" \
              "Модель: {}\n" \
              "Год выпуска: {}\n" \
              "Объём двигателя: {}\n" \
              "Регистрационный номер: {}\n" \
              "Дата регистрации: {}\n" \
              "Номер водительского удостовернеия: {}\n" \
              "Адрес регистрации: {}\n" \
            .format(self.first_name, self.middle_name, self.last_name, self.make, self.model, self.year, self.capacity, self.number_reg, self.data_reg, self.number_drive, self.addres)

    # Запись готовых данных в файл включая только информацию дочернего класса Tehpassport
    def save_f(self):
        fil = str(input("Введите с клавиатуры имя файла для сохранения данных:  "))
        info = self.serialize()
        with open(fil, 'a')as f:
            f.write(str(info))
            f.close()
    # Загрузка  данных из файла включая только информацию дочернего класса Tehpassport
    def load_f(self):
        fil = str(input("Введите с клавиатуры имя файла для загрузки данных, согласно своим записям:  "))
        fi = open(fil, 'r')
        for line in fi.readlines():
            print(line)
        fi.close()
        return fi
# Вызываем все необходимые методы кода
document = Tehpassport()
print(document.input_info_Tehpassport())
print(document.serialize())
print(document.save_f())
print(document.load_f())
print(Tehpassport.mro())
print("Avto <- Tehpasport", issubclass(Avto, Tehpassport))
print("Tehpassport<- Avto", issubclass(Tehpassport, Avto))
print("Man <- Tehpasport", issubclass(Man, Tehpassport))
print("Tehpassport<- Man", issubclass(Tehpassport, Man))
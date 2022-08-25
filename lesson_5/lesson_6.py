# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);

# ● атрибут реализовать как приватный;

# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;

# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;

# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);

# ● проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.


from time import sleep


class TrafficLight:

    __color = ["Красный", "Жёлтый", "Зелёный"]

    def running_method(self):
        print("Запуск")
        sleep(1)
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


t = TrafficLight()
t.running_method()


# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);

# ● значения атрибутов должны передаваться при создании экземпляра класса;

# ● атрибуты сделать защищёнными;

# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;

# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;

# ● проверить работу метода.

# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weigth = 25
        self.heigth = 5

    def weigth_method(self):
        weigth_method = self._length * self._width * self.weigth * self.heigth / 1000
        print(f"Для покрытия дорожного полотна необходимо {weigth_method} массы асфальта")

r = Road(5000, 20)
r.weigth_method()


# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);

# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};

# ● создать класс Position (должность) на базе класса Worker;

# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);

# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):


    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position("Ivan", "Ivanov", "A", "100000", "50000")
print(p.get_full_name(), p.get_total_income())


 # 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);

# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;

# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;

# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go_method(self):
        return (f"Машина {self.name} поехала")

    def stop_method(self):
        return (f"\nМашина {self.name} остановилась")

    def turn_method(self, direction):
        return (f"\nМашина {self.name} повернула {direction}")

    def show_speed(self):
        return (f"Текущая скорость машины {self.name} равна {self.speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            print(f"Вы привышаете допстимую скорость. Ваша скорость {self.speed}")
        else:
            print(f"Ваша скорость в норме.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.speed > 40:
            print(f"Вы привышаете допстимую скорость. Ваша скорость {self.speed}")
        else:
            print(f"Ваша скорость в норме.")


class PoliceCar(Car):
    pass


town = TownCar(70, "Чёрная", "Kia", False)
print("1:\n" + str(town.go_method()), town.show_speed(), town.turn_method("Направо"), town.turn_method("Налево"), town.stop_method())

sport = SportCar(180, "Синяя" , "BMWi8", False)
print("2:\n" + str(sport.go_method()), sport.show_speed(), sport.turn_method("Направо"), sport.stop_method())

work = WorkCar(30, "Белая", "WAZ", False)
print("3:\n" + str(work.go_method()), work.show_speed(), work.turn_method("Налево"), work.stop_method())

police = PoliceCar(90, "Голубая", "Audi", True)
print("4:\n" + str(police.go_method()), work.show_speed(), work.turn_method("Направо"), town.turn_method("Налево"), work.stop_method())


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;

# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);

# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;

# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw_method(self):
        print("Запус отрисовки")

class Pen(Stationery):

    def draw_method(self):
        return (f"Начинаем писать {self.title}")


class Pencil(Stationery):

    def draw_method(self):
        return (f"Начинаем рисовать {self.title}")


class Handle(Stationery):

    def draw_method(self):
        return (f"Начинаем выделять {self.title}")

pen = Pen("ручкой")
print(pen.draw_method())

pencil = Pencil("карандашом")
print(pencil.draw_method())

handle = Handle("маркером")
print(handle.draw_method())
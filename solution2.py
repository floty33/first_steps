from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, brand, battery_level):
        self._brand = brand
        self._battery_level = battery_level

    @abstractmethod
    def charge(self, time):
        pass

    @abstractmethod
    def use(self, hours):
        pass


class Smartphone(Device):
    _device_type = "Смартфон"

    def __init__(self, brand, battery_level, screen_size):
        super().__init__(brand, battery_level)
        self._screen_size = screen_size

    def charge(self, time):
        print(f"Зарядка смартфона '{self._brand}' в течение {time} часов...")
        for hour in range(time):
            if self._battery_level < 100:
                self._battery_level += 10
                if self._battery_level > 100:
                    self._battery_level = 100
                print(f"Уровень заряда: {self._battery_level}%")
            else:
                print(f"Батарея полностью заряжена на {self._battery_level}%.")
                break

    def use(self, hours):
        print(f"Использование зарядки смартфона '{self._brand}' в течение {hours} часов...")
        for hour in range(hours):
            if self._battery_level > 0:
                self._battery_level -= 15
                if self._battery_level < 0:
                    self._battery_level = 0
                print(f"Уровень заряда после {hour+1} часа(ов): {self._battery_level}%")
            else:
                print(f"Батарея разряжена!")
                break

    @staticmethod
    def device_info():
        print(f"Тип устройства: {Smartphone._device_type}")


class Laptop(Device):
    _device_type = "Ноутбук"

    def __init__(self, brand, battery_level, ram_size):
        super().__init__(brand, battery_level)
        self._ram_size = ram_size

    def charge(self, time):
        print(f"Зарядка ноутбука '{self._brand}' в течение {time} часов...")
        for hour in range(time):
            if self._battery_level < 100:
                self._battery_level += 20
                if self._battery_level > 100:
                    self._battery_level = 100
                print(f"Уровень заряда: {self._battery_level}%")
            else:
                print(f"Батарея полностью заряжена на {self._battery_level}%.")
                break

    def use(self, hours):
        print(f"Использование зарядки ноутбука '{self._brand}' в течение {hours} часов...")
        for hour in range(hours):
            if self._battery_level > 0:
                self._battery_level -= 25
                if self._battery_level < 0:
                    self._battery_level = 0
                print(f"Уровень заряда после {hour+1} часа(ов): {self._battery_level}%")
            else:
                print(f"Батарея разряжена!")
                break

    @staticmethod
    def device_info():
        print(f"Тип устройства: {Laptop._device_type}")


phone = Smartphone("Samsung", 50, 6.5)
laptop = Laptop("Huawei", 30, 16)

Smartphone.device_info()

phone.charge(4)

phone.use(7)

Laptop.device_info()

laptop.charge(3)

laptop.use(3)

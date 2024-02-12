class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def display_info(self):
        return Car


class Motorcycle(Vehicle):
    def __(self, brand, year, speed):
        super().__init__(brand, year)
        self.speed = speed

    def display_info(self):
        return Motorcycle



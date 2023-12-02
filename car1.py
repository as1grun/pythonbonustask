class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Camry", 2022)

car1.display_car()

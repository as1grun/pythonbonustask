class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, km):
        self.mileage += km
        print(f"Mileage after driving {km} km: {self.mileage}")

    def display_car(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Camry", 2022, "Blue", 15000)

car1.drive(100)

class ElectricCar(Car):
    def __init__(self, make, model, year, color, mileage, battery_size):
        super().__init__(make, model, year, color, mileage)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery size: {self.battery_size} kWh")

electric_car = ElectricCar("Tesla", "Model S", 2023, "Black", 5000, 75)

electric_car.display_car()
electric_car.describe_battery()

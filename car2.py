class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

car1 = Car("Toyota", "Camry", 2022, "Blue", 15000)
car2 = Car("Honda", "Accord", 2021, "Red", 20000)

print(f"Car 1: {car1.color} {car1.year} {car1.make} {car1.model}, Mileage: {car1.mileage}")
print(f"Car 2: {car2.color} {car2.year} {car2.make} {car2.model}, Mileage: {car2.mileage}")

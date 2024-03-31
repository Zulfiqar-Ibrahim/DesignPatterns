class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def __str__(self):
        return f"Car: {self.year} {self.make} {self.model}, Color: {self.color}"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make

    def set_model(self, model):
        self.car.model = model

    def set_year(self, year):
        self.car.year = year

    def set_color(self, color):
        self.car.color = color

    def get_car(self):
        return self.car
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self, make, model, year, color):
        self.builder.set_make(make)
        self.builder.set_model(model)
        self.builder.set_year(year)
        self.builder.set_color(color)
        return self.builder.get_car()
if __name__ == "__main__":
    builder = CarBuilder()
    director = CarDirector(builder)

    car_1 = director.construct_car("Toyota", "Camry", 2022, "Red")
    print(car_1)
    car_2 = director.construct_car("Mercedeze", "A10", 2022, "black")
    print(car_1)
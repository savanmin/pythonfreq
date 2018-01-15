class Car:
    def __init__(self, year, price):
        self.year = year
        self.price = price

    def about(self):
        print("Year of the car is %d and price is %d " % (self.year, self.price), end=" ")


class Honda(Car):
    def __init__(self, year, price, model):
        Car.__init__(self, year, price)
        self.model = model

    def about(self):
        Car.about(self)
        print("Model is %s " % self.model)


class Toyota(Car):
    def __init__(self, year, price, model):
        Car.__init__(self, year, price)
        self.model = model

    def about(self):
        Car.about(self)
        print("Model is %s " % self.model)


car_1 = Toyota(2016, 20000, "city")
Toyota.about(car_1)

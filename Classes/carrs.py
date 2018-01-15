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


class Civic(Honda):





class Toyota(Car):
    def __init__(self, year, price, model):
        Car.__init__(self, year, price)
        self.model = model

    def about(self):
        Car.about(self)
        print("Model is %s " % self.model)


class Innova(Toyota):



while True:
    print()
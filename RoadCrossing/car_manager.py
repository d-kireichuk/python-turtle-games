from car import Car
import random

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = 0.1
        self.car_density = 10

    def create_car(self):
        if random.randint(1, self.car_density) == self.car_density:
            self.cars.append(Car())

    def increase_car_density(self):
        if self.car_density >= 4:
            self.car_density -= 1

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)

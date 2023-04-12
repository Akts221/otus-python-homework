from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def __str__(self):
        return f"{self.weight, self.fuel, self.fuel_consumption}"

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                self.started = False
                raise LowFuelError

    def move(self, distance):
        max_distance = self.fuel / self.fuel_consumption
        if max_distance <= 0:
            raise NotEnoughFuel
        elif max_distance < distance:
            raise NotEnoughFuel
        else:
            self.fuel = self.fuel - (distance * self.fuel_consumption)
            return self.fuel


car_1 = Vehicle(23.0, 2, 7.0)
car_1.start()

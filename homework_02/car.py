"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
import engine


class Car(Vehicle):

    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def __str__(self):
        return f"{self.weight, self.fuel, self.fuel_consumption}"

    def set_engine(self, engine_1):
        self.engine = engine_1


car_2 = Car(2.3, 22, 22)
print(car_2.set_engine(engine.Engine_1))

"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_people):
        cargo_current = cargo_people + self.cargo
        if self.max_cargo < cargo_current:
            raise CargoOverload
        else:
            self.cargo = cargo_current
            return self.cargo


    def remove_all_cargo(self):
        do_ouk = self.cargo
        self.cargo = 0
        return do_ouk


plane_1 = Plane(23.0, 14.0, 3.0, 20)
plane_1.load_cargo(2)
plane_1.remove_all_cargo()

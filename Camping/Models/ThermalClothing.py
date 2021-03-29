from Models.Camping import CampingItem
from Models import enum_material_thermal_clothing


class ThermalClothing(CampingItem):
    def __init__(self, name: str, producer: str, weight_in_grams: int, price: int,
                 material_thermal_clothing: enum_material_thermal_clothing.MaterialTermalClothing):
        super().__init__(name, producer, weight_in_grams, price)
        self.__material_thermal_clothing = material_thermal_clothing

    @property
    def material_thermal_clothing(self):
        return self.__material_thermal_clothing

    def __str__(self):
        return f"""{super().__str__()} Material thermal clothing: {self.__material_thermal_clothing}"""

from Models.Camping import CampingItem
from Models import enum_material_thermal_clothing


class ThermalClothing(CampingItem):
    def __init__(self, _name: str, _weight_in_grams: int, _price: int,
                 _material_thermal_clothing: enum_material_thermal_clothing.MaterialTermalClothing):
        super().__init__(_name, _weight_in_grams, _price)
        self._material_thermal_clothing = _material_thermal_clothing

    @property
    def material_thermal_clothing(self):
        return self._material_thermal_clothing

    def __str__(self):
        return f"""{super().__str__()}| Material thermal clothing: {self._material_thermal_clothing}"""

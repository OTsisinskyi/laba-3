from Models.Camping import CampingItem
from Models import enum_raincoat_type
from Models import enum_materials_type


class Raincoat(CampingItem):
    def __init__(self, name: str, weight_in_grams: int, price: int, materials: enum_materials_type.MaterialsType,
                 raincoat_type: enum_raincoat_type.RaincoatType):
        super().__init__(name, weight_in_grams, price)
        self.__materials = materials
        self.__raincoat_type = raincoat_type

    @property
    def materials(self):
        return self.__materials

    @property
    def raincoat_type(self):
        return self.__raincoat_type

    def __str__(self):
        return f"""{super().__str__()}| Material: {self.__materials}| \
 Raincoat type: {self.__raincoat_type}"""

from Models.Camping import CampingItem
from Models import enum_filler


class SleepingBag(CampingItem):
    def __init__(self, name: str, weight_in_grams: int, price: int, filler: enum_filler.Filler):
        super().__init__(name, weight_in_grams, price)
        self.__filler = filler

    @property
    def filler(self):
        return self.__filler

    def __str__(self):
        return f"""{super().__str__()} Filler: {self.__filler}"""

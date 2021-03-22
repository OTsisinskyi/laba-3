from Models.Camping import CampingItem
from Models import enum_view_type


class Backpack(CampingItem):
    def __init__(self, name: str, weight_in_grams: int, price: int,
                 internal_volume: int, view: enum_view_type.ViewType):
        super().__init__(name, weight_in_grams, price)

        self.__internal_volume = internal_volume
        self.__view = view

    @property
    def internal_volume(self):
        return self.__internal_volume

    @property
    def view(self):
        return self.__view

    def __str__(self):
        return f"""{super().__str__()}| The volume of the backpack: {self.__internal_volume}|\
 Type of backpack: {self.__view}"""

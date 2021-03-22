from abc import ABC
from abc import abstractmethod


class CampingItem(ABC):
    def __init__(self, name: str, weight_in_grams: int, price: int):
        self._name = name
        self._weight_in_grams = weight_in_grams
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def weight_in_grams(self):
        return self._weight_in_grams

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"""Product name: {self.name} --- Weight: {self.weight_in_grams} gram\n"""

    @abstractmethod
    def __str__(self):
        return f"""Name: {self.name}| Weight in grams: {self.weight_in_grams}| Price: {self.price} UAN|"""

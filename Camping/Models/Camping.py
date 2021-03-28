class CampingItem(object):
    def __init__(self, name: str, producer: str, weight_in_grams: int, price: int):
        self._name = name
        self._producer = producer
        self._weight_in_grams = weight_in_grams
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def producer(self):
        return self._producer

    @property
    def weight_in_grams(self):
        return self._weight_in_grams

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"""Producer - {self._producer} | Name - {self.name} | Weight - {self.weight_in_grams} gram\n"""

    def __str__(self):
        return f"""Name: {self.name}|Producer: {self._producer}|Weight in grams: {self.weight_in_grams}| Price: {self.price} UAN|"""

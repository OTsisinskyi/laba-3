class CampingManager(object):
    def __init__(self, items: list):
        self.items = items

    def sort_by_weight(self, reverse: bool = False):
        return sorted(self.items, key=lambda weight: weight.weight_in_grams, reverse=reverse)

    def sort_by_producer(self, reverse: bool = False):
        return sorted(self.items, key=lambda weight: weight.producer, reverse=reverse)

    def find_item(self, goods):
        for i in self.items:
            if i == goods:
                return i
            else:
                return print("Not in listed!!!")

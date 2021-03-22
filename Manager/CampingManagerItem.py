from Models import enum_sort_order


class CampingManager(object):
    def __init__(self, items: list):
        self.items = items

    def sort_by_weight(self, sort_order: enum_sort_order.SortOrder):
        if sort_order == enum_sort_order.SortOrder.ASC:
            weight_list = sorted(self.items, key=lambda weight: weight.weight_in_grams, reverse=False)
            print(weight_list)
        else:
            weight_list = sorted(self.items, key=lambda weight: weight.weight_in_grams, reverse=True)
            print(weight_list)
        return " "

    def find_item(self, name):
        if [x for x in self.items if x.name == name]:
            print(f"""{name} - is in the list""")
        else:
            print(f"""{name} - not listed""")
        return " "

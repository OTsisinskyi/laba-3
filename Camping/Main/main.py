from Models import *
from Manager import *


def main():
    tent = Tent("Tent", "Armot", 4100, 2100, 4, 5,
                enum_appointment_type.AppointmentType.GROUP)

    sleeping_bag = SleepingBag("Sleeping bag", "BUECHUA", 810, 1269,
                               enum_filler.Filler.FLUFF)

    food_set = FoodSet("Food set", "Food_tyt", 700, 850, 4000, 20,
                       enum_appointment_type.AppointmentType.PERSONAL)

    back_pack = Backpack("Back pack", "Terra Incognita ", 2265, 3499, 40,
                         enum_view_type.ViewType.FRAME)

    first_aid_fit = FirstAidFit("First aid fit", "Help_tyt", 436, 670,
                                enum_appointment_type.AppointmentType.PERSONAL)

    raincoat = Raincoat("Raincoat", "Runok", 120, 230, enum_materials_type.MaterialsType.GORTEX,
                        enum_raincoat_type.RaincoatType.LONG)

    thermal_clothing = ThermalClothing("Thermal clothing", "CUNISHER-STATIC", 150, 500,
                                       enum_material_thermal_clothing.MaterialTermalClothing.WOOL)

    camping_item = [tent, sleeping_bag, food_set, back_pack, first_aid_fit, raincoat, thermal_clothing]
    list_result = CampingManager(camping_item)

    print(tent.__str__())
    print(sleeping_bag.__str__())
    print(food_set.__str__())
    print(back_pack.__str__())
    print(first_aid_fit.__str__())
    print(raincoat.__str__())
    print(thermal_clothing.__str__())
    print("")
    print("The product we were looking for:")
    print(list_result.find_item(tent))
    print("")
    print("The goods are sorted by weight:")
    print(list_result.sort_by_weight(False))
    print("")
    print("Sorted list of manufacturers:")
    print(list_result.sort_by_producer(True))


if __name__ == '__main__':
    main()

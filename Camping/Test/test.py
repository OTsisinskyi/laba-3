import unittest
from Models import *
from Manager import *


class TestCampingManager(unittest.TestCase):
    def setUp(self):
        self.tent = Tent("Tent", "Armot", 4100, 2100, 4, 5,
                         enum_appointment_type.AppointmentType.GROUP)

        self.sleeping_bag = SleepingBag("Sleeping bag", "BUECHUA", 810, 1269,
                                        enum_filler.Filler.FLUFF)

        self.food_set = FoodSet("Food set", "Food_tyt", 700, 850, 4000, 20,
                                enum_appointment_type.AppointmentType.PERSONAL)

        self.back_pack = Backpack("Back pack", "Terra Incognita ", 2265, 3499, 40,
                                  enum_view_type.ViewType.FRAME)

        self.first_aid_fit = FirstAidFit("First aid fit", "Help_tyt", 436, 670,
                                         enum_appointment_type.AppointmentType.PERSONAL)

        self.raincoat = Raincoat("Raincoat", "Runok", 120, 230, enum_materials_type.MaterialsType.GORTEX,
                                 enum_raincoat_type.RaincoatType.LONG)

        self.thermal_clothing = ThermalClothing("Thermal clothing", "CUNISHER-STATIC", 150, 500,
                                                enum_material_thermal_clothing.MaterialTermalClothing.WOOL)

        self.camping_item = [self.tent, self.sleeping_bag, self.food_set, self.back_pack,
                             self.first_aid_fit, self.raincoat, self.thermal_clothing]

        self.list_result = CampingManager(self.camping_item)

    def test_sort_by_weight(self):
        self.assertEqual(self.list_result.sort_by_weight(True), [self.tent, self.back_pack, self.sleeping_bag,
                                                                 self.food_set, self.first_aid_fit,
                                                                 self.thermal_clothing, self.raincoat])

    def test_sort_by_producer(self):
        self.assertEqual(self.list_result.sort_by_producer(False), [self.tent, self.sleeping_bag, self.thermal_clothing,
                                                                    self.food_set, self.first_aid_fit, self.raincoat,
                                                                    self.back_pack])

    def test_find_item(self):
        self.assertEqual(self.list_result.find_item(self.tent), self.tent)

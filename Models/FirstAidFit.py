from Models.Camping import CampingItem
from Models import enum_appointment_type


class FirstAidFit(CampingItem):
    def __init__(self, name: str, weight_in_grams: int, price: int,
                 appointment: enum_appointment_type.AppointmentType):
        super().__init__(name, weight_in_grams, price)
        self.__appointment = appointment

    @property
    def appointment(self):
        return self.__appointment

    def __str__(self):
        return f"""{super().__str__()}| Appointment: {self.__appointment}"""

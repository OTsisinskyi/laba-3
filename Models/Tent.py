from Models.Camping import CampingItem
from Models import enum_appointment_type


class Tent(CampingItem):
    def __init__(self, name: str, weight_in_grams: int, price: int, capacity_of_people: int,
                 square_tent: int, appointment: enum_appointment_type.AppointmentType):
        super().__init__(name, weight_in_grams, price)
        self.__appointment = appointment
        self.__capacity_of_people = capacity_of_people
        self.__square_tent = square_tent

    @property
    def appointment(self):
        return self.__appointment

    @property
    def capacity_of_people(self):
        return self.__capacity_of_people

    @property
    def square_tent(self):
        return self.__square_tent

    def __str__(self):
        return f"""{super().__str__()} Appointment:{self.__appointment}| Capacity of people:{self.__capacity_of_people}|\
  Square tent: {self.__square_tent}"""

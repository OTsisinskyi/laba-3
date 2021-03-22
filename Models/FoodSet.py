from Models.Camping import CampingItem
from Models import enum_appointment_type


class FoodSet(CampingItem):
    def __init__(self, name: str, weight_in_grams: int, price: int,
                 caloric_content: int, expiration_date: int, appointment: enum_appointment_type.AppointmentType):
        super().__init__(name, weight_in_grams, price)

        self.__appointment = appointment
        self.__caloric_content = caloric_content
        self.__expiration_date = expiration_date

    @property
    def appointment(self):
        return self.__appointment

    @property
    def caloric_content(self):
        return self.__caloric_content

    @property
    def expiration_date(self):
        return self.__expiration_date

    def __str__(self):
        return f"""{super().__str__()} Appointment: {self.__appointment}|\
 Caloric content: {self.__caloric_content}| Expiration data:{self.__expiration_date}"""

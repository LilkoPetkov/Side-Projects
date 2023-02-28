from abc import ABC, abstractmethod


class Doctor(ABC):
    def __init__(self, name, phone_number, hospital, description):
        self.name = name
        self.phone_number = phone_number
        self.hospital = hospital
        self.appointments = []
        self.description = description

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) != 10 or not all(s.isdigit() for s in value):
            raise ValueError("Phone numbers should have 10 characters and only digits.")
        self.__phone_number = value

    @abstractmethod
    def add_appointments(self, *args):
        pass

    def __str__(self):
        return f"Doctor {self.name} - {self.phone_number} - {self.hospital}. Appointments:\
 {', '.join(s for s in self.appointments)} - \
{self.description}."

import re


class Person:
    def __init__(self, first_name, last_name, email="_@_.__", phone="0100000000"):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self._age = -1
        if re.findall(r"^[-\w\.]+@([\w-]+\.)+[\w-]{2,4}$", email):
            self.email = email
        else:
            print(f"Mauvais email {email}")
            self.email = "_@_.__"
        if re.findall(
                r"^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$",
                phone):
            self.phone = phone
        else:
            print(f"Mauvais numéro de téléphone {phone}")
            self.phone = "0100000000"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone}"

    def set_age(self, age):
        if age in range(0, 110):
            self._age = age

    def get_age(self):
        return self._age

    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return True
        else:
            return False

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

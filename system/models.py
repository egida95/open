from random import choice
from datetime import datetime


class University:
    def __init__(self, name: str, location: str, list_direction: list) -> None:
        self.name = name
        self.location = location
        self.list_direction = list_direction
    
    def info(self):
        return f"Название: {self.name}   Место нахождение: {self.location}\
             \nНаправления:  {self.list_direction}"
    
    def __str__(self) -> str:
        return self.name

class Cart:
    def __init__(self, name: str) -> None:
        self.name = name
        self.number = self._gen_number()
        self.date = datetime.today()
        self.cv = self._gen_cv()
        self.balance = 0
    
    def __str__(self) -> str:
        return self.name + ' баланс: ' + self.balance
    
    def _gen_number(self):
        number = ''
        for i in range(1, 17):
            number += choice('1234567890')
            if i % 4 == 0:
                number += " "
        return number
    
    def _gen_cv(self):
        cv = ''
        for _ in range(2):
            cv += choice('1234567890')
        return cv

class Student:
    def __init__(self, full_name: str, university: University, start_year: int, cart: Cart = None) -> None:
        self.full_name = full_name
        self.university = university
        self.start_year =start_year
        self.cart = cart

    def __str__(self) -> str:
        return str(self.full_name)

    def get_balace(self):
        if self.cart:
            return self.cart.balance
        else:
            return "u studenta netu kart"
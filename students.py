class University:
    def init(self, name: str, location: str, list_direction: list) -> None:
        self.name = name
        self.location = location
        self.list_direction = list_direction
    
    def info(self):
        return f"Название: {self.name}   Место нахождение: {self.location}\
             \nНаправления:  {self.list_direction}"
    
    def str(self) -> str:
        return self.name


class Cart:
    def init(self,number: str,date: str,cv: int,balance: int) -> None:
        self.number = number
        self.date = date
        self.cv = cv
        self.balance = balance
    
    def str(self) -> str:
        return self.number
    
class Student:
    def init(self, full_name: str, university: University, start_year: int, cart: Cart = None) -> None:
        self.full_name = full_name
        self.university = university
        self.start_year = start_year
        self.cart = cart

    def str(self) -> str:
        return str(self.full_name)

manas = University('Manas', 'Manasa 165', ['programmimg', 'Git', 'Doctor', 'Electrik', 'Dev'])
politeh = University("Политехнический Университет", "Ahunbeava", ['programmimg', 'Git', 'Doctor', 'Electrik'])


tilek = Student("Tilekov Tilek Tilekovich", manas, 2020)
bael = Student("Tilekov Bael Asanovich", politeh, 2021)
argen = Student("Tilekov Argen Baelevich", manas, 2020)

univers = [manas, politeh]
students = [tilek, bael, argen]
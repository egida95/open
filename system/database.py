from models import Student, Cart, University 

# univer 
manas = University('Manas', 'Manasa 165', ['programming','doctor','Git','Santehnika'])
politeh = University('Politeh', 'Ahunbaeva', ['programming','doctor','Git','Santehnika'])

# Students 
tilek = Student('Tilekov Tilek Tilekovich', manas, 2020)
bael = Student('Tilekov Bael Asanovich', politeh, 2021)
argen = Student('Tilekov Argen Baelevich', manas, 2020)


univers = [manas, politeh]
students = [tilek, bael, argen]
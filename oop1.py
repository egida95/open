# class Product:
#     name = 'Фен'
#     prise = 123
#     desic = 'Из Германии'
#     code = 1234567
    

# p = Product()

# p.price = 345
# print(p.prise)   
# print(p.name)



# class car:
#     name = 'BMW'
#     mark = 'm678'
#     color = 'black'
#     motor = 'M1'
    
# s = car()

# print(s.color)



# class Cat:
#     def __init__(self,name,poroda,age) -> None:
#         self.name = name 
#         self.poroda = poroda 
#         self.age = age
            
#     def run(self):
#         print('побежал')
    
#     def murl(self):
#         print(f'{self.name}мяукнул')
    
# tom = Cat('Toм', 'poroda', 2)
# ken = Cat('Keн', 'poroda', 5)

# cats = [tom,ken]

# count = 0 
# for i in cats:
#     count += i.age
    
# for i in cats:
#     i.murl() 

    
# a = Cat()
# r = Cat()
# r.name = 'Ween'

# a.murl()
# r.run()


# a.name = 'Eren'
# print(a.name)
# a.run()

# for _ in range(1,11):
#     a.murl()
    
    

# создать класс Course
# atrrs:
#    name = str
#    dlitelnost = str 
#    napravlenie = str


# создать класс Student
# atrrs:
#       full name = str
#       email = str
#       phone = str 
#       course = object 
#       studies = bool
#        comment = str







class Course:
    def __init__(self,name,dlitelnost,napravlenie) -> None:
        self.name = name 
        self.dlitelnost = dlitelnost
        self.napravlenie = napravlenie
        
b = Course('IT', 5,'backend')

# print(b.name)


class Student:
    def __init__(self,full_name,email,phone,course,studies,comment) -> None:
        self.full_name = full_name 
        self.email = email
        self.phone = phone
        self.course = course  
        self.studies = studies
        self.comment = comment
    
    
    def __str__(self):
        return f'Student name = {self.phone}'
    
        
s = Student('Shoto', 'shotogmail.com', 123456, b, 'asdfg', 'qwerty')

print(s.full_name)
        
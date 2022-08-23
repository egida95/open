from models import Student, Cart, University
from database import tilek, bael, argen, students, univers

tilek.cart = Cart('Tileksila')
bael.cart = Cart('Apalone')
argen.cart = Cart('Segatike')

tilek.cart.balance += 5000

print(tilek.cart.balance)

def give_money(sender, resiver, summ):
    if sender.cart.bolans > summ:
        sender.cart.balance -= summ
        resiver.cart.balance += summ
        print(f'{sender.name} uspeshno otpravilos {resiver.name} {summ} com')
        
    else:
        print(f'u {sender.name} ne hvataet deneg')
        
        
    give_money(tilek, bael, 500)
    

while True:
    a = input('Vyberete deystvie \n1. spisok studentov \n2. info univer \n3. send money')
    if a == '1':
        for i in students:
            print(i) 
            
    elif a == '2':
        for i in univers:
            print(i.info())
            
    elif a == '3':
        for i,name in enumerate(students):
            print(i, name) 
        sender = int(input('vyberi otpravitely: '))
        sender = students(sender) 
        resiver = int(input('vyberi summu: '))
        give_money(sender, resiver, summ) 

        print(f'{sender.full_name} ostalos {sender.cart_balance}')
        print(f'{resiver.full_name} stalo {sender.cart_balance}')


    elif a == '4':
        for i, name in enumerate(students):
            print(i, name)
        student = int(input("vybery otpravitla: "))
        student = students[student]
        print(student.cart)

# tilek.cart.balance -= 500 
# bael.cart.balance += 500

# tilek.cart.balance -= 1000
# bael.cart.balance += 1000

# print()    
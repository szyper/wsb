import os

def wyswietl(num1, num2):
    print(f'Liczba 1: {num1}')
    print(f'Liczba 2: {num2}')

wyswietl(2, 4)

####################  *args  #####################
print('####################  *args  #####################')

def wyswietlArgs(num1, *args):
    print(f'\nLiczba 1: {num1}')
    for i in args:
        print(f'Następna wartość: {i}')

wyswietlArgs(1, 12, 1000, 211, 2)

############

imiona = ['Anna', 'Jan', 'Paweł']
wyswietlArgs(imiona)
wyswietlArgs(*imiona)

os.system('cls')

####################  *kwargs  #####################
print('####################  **kwargs  #####################')

def pracownik(**kwargs):
    for key, val in kwargs.items():
        print(f'Klucz {key}, wartość {val}')

pracownik1 = {
    'imie':'Janusz',
    'nazwisko':'Kowalski',
    'wiek':21,
    'umowaOprace': True
}

pracownik(**pracownik1)

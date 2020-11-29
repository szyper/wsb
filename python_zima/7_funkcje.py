def witaj():
    print('Witaj Janusz!')

witaj()

def wyswietlWiek(wiek):
    print(f'Twój wiek: {wiek}')

wyswietlWiek(23)

def iloczyn(a, b):
    return a * b

print(iloczyn(3, 4))

def iloraz(a, b):
    return a / b

iloraz1 = iloraz(3, 4)
print(iloraz1)
print(type(iloraz1))

print(iloraz(b=5, a=2))

'''
Użytkownik podaje z klawiatury:
marka, model, pojemnosc, predkoscMax
utwórz funkcję, która pobierze dane od użytkownika i przypisze do słownika
utwórz drugą funkcję wyświetlającą dane w formacie:
Marka: ...
Model: ...
Pojemnosc: ...
Predkosc maksymalna: ...
'''

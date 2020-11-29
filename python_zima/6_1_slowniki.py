slownik = {'klucz1':'wartosc1', 'klucz2':'wartosc2'}

'''
    Utwórz słownik o nazwie pracownik zawierający klucze:
    imie, nazwisko, miasto, wiek, imionaDzieci, imionaRodzicow
'''
pracownik = {
    'imie':'Anna',
    'nazwisko':'Nowak',
    'miasto':'Poznań',
    'wiek':23,
    'imionaDzieci':['Anna', 'Tomasz'],
    'imionaRodzicow':['Julia', 'Paweł']
}

print(pracownik)
print(pracownik['imionaDzieci'])
print(pracownik['imionaDzieci'][0])

pracownik['wzrost'] = 175
pracownik['waga'] = 75
print(pracownik)

##################################

pracownik1 = {
    'imie':'Anna',
    'nazwisko':'Nowak',
    'miasto':'Poznań',
    'wiek':23
}

print()
print(pracownik1)

klucz = 'wiek'
if klucz in pracownik1:
    del pracownik1[klucz]
    print(f'Klucz {klucz} został usunięty')
else:
    print(f'Klucz {klucz} nie został usunięty')

print(pracownik1)
print(pracownik1.keys())
print(pracownik1.values())
print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=' ')

print()

for key, value in pracownik1.items():
    print(f'{key}: {value}')

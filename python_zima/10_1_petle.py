#pętle zadania

'''
    Podaj wartość początkową i końcową, która będzie wypisana w porządku nierosnącym
'''




x = int(input('Podaj x: '))
y = int(input('Podaj y: ')) - 1

if y > x:
    pom = x
    x = y + 1
    y = pom - 1

for i in range(x, y, -1):
    print(f'{i} ',end=' ')

print()

'''
*
**
***
****
*****
'''

for i in range(1,6):
    for j in range(1,i+1):
        print('*', end='')
    print()

print()
i = 1
ilosc = int(input('Ilość wierszy: ')) + 1
znak = input('Znak: ')
print()

for i in range(1, ilosc):
    print(znak * i)
    i = i + 1
print()

#####################################
#zad 1

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))

suma = a + b
if suma == 0:
    print('Próba dzielenia przez zero')
else:
    dzialanie = (a*a+b)/((a+b)*(a+b))

if suma != 0:
    print(f'Wartość wyrażenia wynosi: {dzialanie}')

#try except

#####################################

school = 'CDV Poznan'

for letter in school:
    if letter == 'V' or letter == ' ':
        continue
    print(f'Litera: {letter}')

print()

#####################################

x = 10
while x > 0:
    x = x - 1
    if x == 6:
        continue
    print(f'{x} ', end=' ')
print('Koniec programu!')

'''
    Użytkownik podaje z klawiatury hasło,
    jeśli poda hasło: 'okon' to na ekranie wyświetli się komunikat: 'Poprawne hasło'
    Użytkownik ma na podanie hasła trzy próby
    Jeśli przekroczy ilość prób to na ekranie wyświetli mu się komunikat: 'Przekroczono limit prób podania hasła'
'''

import os
os.system('cls')

password = input('Podaj hasło: ')
count = 1

while password != 'okon' and count != 3:
    count = count + 1
    password = input('Podaj hasło: ')

if password == 'okon':
    print(f'Hasło odgadnięto za {count} próbą')

if count == 3 and password != 'okon':
    print('Przekroczono limit prób podania hasła!')

if password == 'okon':
    print('Poprawne hasło')

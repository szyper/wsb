print("test")
print(8)

x = 10.1234
print(x)
print("{:.2f}".format(x))

#potęgowanie
pow=2**10
print(pow)

'''
pobieranie danych
z klawiatury
'''

#konkatenacja +
name=input()
print("Twoje imię: " + name)

surname=input("Podaj swoje nazwisko")
print("Twoje imię: " + name + ", nazwisko: " + surname)

'''
Użytkownik1 podaje z klawiatury swoje dane: imie, nazwisko i wiek
Użytkownik2 podaje z klawiatury swoje dane: imie, nazwisko i wiek

wyświetl dane w formacie:

User1: imie i nazwisko, wiek: ...
User2: imie i nazwisko, wiek: ...
Średni wiek: ... (precyzja 2 miejsca po przecinku)
'''

print("\nPodaj swój wiek: ", end="")
age=input()

surname="Kowalski"
firstLetter = surname[0]
print(firstLetter)

lastLetter1=surname[len(surname) -1]
lastLetter2=surname[-1]
print(lastLetter1)
print(lastLetter2)

#konwersja typu 
x="5"
print(type(x))

y=4
print(type(y))
y=y/2
print(type(y))
print(y)

surname="Kowalski"
print()
print(surname[0]) #K
print(surname[0:3]) #Kow
print(surname[-2]) #k
print(surname[-2:]) #ki
print(surname[:-2]) #Kowals
print(surname[:-2:2]) #Kwl
text="Anna, Krystyna, Tomasz"

tab = text.split(", ")
print(text)
print(tab)
print(type(tab))

name1=tab[0]
print(name1)

nameUpper=name1.upper()
print(nameUpper)

nameLower=name1.lower()
print(nameLower)

#sprawdzenie zawartości
surname=input("Podaj nazwisko:")
content=surname.isalpha()
print(content)

text1="Jan\n"
text2="Nowak"
print(text1 + text2)

text1=text1.rstrip()
print(text1 + " " + text2)

#wyświetlenie łańcucha znaków
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje Python > 2.6
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie daty
year=2020
month=10
day=4

print("Data: ",end="")
print(day, month, year)

print(day, month, year, sep="-")

#data pobrana z systemu
from datetime import date
today=date.today()
print("Dzisiejsza data: ", today)

# dd-mm-YY
data = today.strftime("%d-%m-%Y")
print("data: ", data)

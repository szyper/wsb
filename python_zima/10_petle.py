#Pętla FOR

colors = ['red', 'green', 'blue', 'magenta']
print(colors)
print(type(colors))

for color in colors:
    print(color)

print('\n')

#Wypisz tekst
string = 'CDV - uczelnia ludzi ciekawych'
for letter in string:
    print(letter,end=" ")
print()
#Wypisz liczby od 1-10
for number in range(1, 11):
    print(number,end=" ")

print()

#Wypisz elementy z listy do momentu wartości 'end', 'q', 'quit'

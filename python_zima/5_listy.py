programowanie = ['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print(pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatniElement = programowanie[-1]
print(ostatniElement)

# Dodanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

# Zliczanie elementów w liście
ile = programowanie.count('Python')
print(ile)

# Ilość elementów w liście
iloscElem = len(programowanie)
print(iloscElem)

#  polaczenie list
inneJezyki = ['C', 'C++']
programowanie.extend(inneJezyki)
print(programowanie)

# Czyszczenie list
nowa = programowanie
print('Lista nowa: ',end="")
print(nowa)
nowa.clear()
print('Lista nowa: ',end="")
print(nowa)
print('Lista programowanie: ',end="")
print(programowanie)

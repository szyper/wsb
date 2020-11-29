#listy
imiona = ['Julia', 'Anna', 'Krystyna']
print(type(imiona)) #<class 'list'>
imiona.append('Janusz')
ilosc = len(imiona)
print(f'Ilość imion: {ilosc}')

#tuple
nazwiska = ('Kowalski', 'Nowak')
print(type(nazwiska)) #<class 'tuple'>
print(nazwiska)

#słowniki
osoba = {
    'imie':'Julia',
    'nazwisko':'Nowak',
    'wiek':23
}

print(osoba)
print(type(osoba)) #<class 'dict'>
print(osoba['nazwisko'])
print(osoba.keys()) #dict_keys(['imie', 'nazwisko', 'wiek'])
print(osoba.get('wzrost', 'Brak danych'))
print(osoba.get('imie', 'Brak danych'))

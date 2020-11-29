#Przekazywanie argumentów przez referencję

def show(name):
    print(f'Przed modyfikacją: {name}')
    # print('Przed modyfikacją:',name)
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'Po modyfikacji: {id(name)}')

data = ['Anna', 'Agnieszka', 'Andrzej']

print(f'Przed wywołaniem funkcji show: {data}')
print(f'Id obiektu: {id(data)}')

show(data)

print(f'Po wywołaniu funkcji show: {data}')

################### słownik ##################

data1 = {
    0:'Artur',
    1:'Andrzej'
}

print(f'\nPrzed wywołaniem funkcji show: {data1}')
show(data1)

#Przekazywanie argumentów przez wartość
print('\n#######  Przekazywanie argumentów przez wartość\n')

def show1(city):
    print(f'Przed modyfikacją: {city}')
    city[0] = 'Berlin'
    city[1] = 'Bukareszt'
    print(f'Po modyfikacji: {city}')
    print(f'Po modyfikacji: {id(city)}')

miasto = ['Poznań', 'Gniezno']
print(f'Przed wywołaniem funkcji show1: {miasto}')
print(f'Id obiektu: {id(miasto)}')
show1(list(miasto))
print(f'Po wywołaniu funkcji show1: {miasto}')

################### słownik ##################
print('\n#######  Przekazywanie argumentów przez wartość słownik\n')

miasto1 = {
    0:'Poznań',
    1:'Gniezno'
}
print(f'Przed wywołaniem funkcji show1: {miasto1}')
print(f'Id obiektu: {id(miasto1)}')
show1(dict(miasto1))
print(f'Po wywołaniu funkcji show1: {miasto1}')

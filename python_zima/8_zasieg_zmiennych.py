#Zasięg zmiennych, zmienne lokalne i globalne

#precyzja liczby (zaokrąglenie do 3 miejsc po przecinku liczby 5: 5.000)
x = "{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = "{0:.4f}".format(iloscChf)
    print(iloscChf)

plnToChf(1000)

'''
    Utwórz funkcję zwracającą ilość Euro jaką klient może kupić za PLN
'''
def plnToEuro(value):
    kursEuro = 3.7913
    iloscEuro = value / kursEuro
    iloscEuro = "{0:.0f}".format(iloscEuro)
    print(iloscEuro)

plnToEuro(1000)

#zmienna globalna
kursUSD = 3.50
print(f'Id USD: {id(kursUSD)}')

def plnToUSD(value):
    kursUSD = 4.00
    iloscUSD = value / kursUSD
    iloscUSD = "{0:.4f}".format(iloscUSD)
    print(f'Id USD wewnątrz funkcji: {id(kursUSD)}')
    return iloscUSD

print(f'\nKurs dolara: {kursUSD}')
pln = input('Podaj kwotę PLN jakie chcesz zamieniń na USD: ')
usd = plnToUSD(float(pln))
print(f'Ilość {pln}PLN = {usd}USD')
print(f'\nKurs dolara po wywołaniu funkcji: {kursUSD}')

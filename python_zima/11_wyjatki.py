'''
x = 2
y = 0
wynik = x / y
'''

def iloraz(x, y):
    try:
        # result = x / y
        result = x // y
        print(f'Wynik dzielenia {x} / {y} wynosi: {result}')
    except ZeroDivisionError:
        print('Dzielenie przez zero!')

# iloraz(2, 5)
#iloraz(2, 0)
iloraz(30, 12)

x=6

if x==5:
  print("x jest równe 5")
else:
  print("x nie jest równe 5")
  print("x jest równe: ", x)

y=False
if y:
  print('prawda')
else:
  print('fałsz')

k=input('Podaj k:')
if bool(k):
  print('k zawiera dane: ',k)
else:
  print('k nie zawiera danych')

'''
  Użytkownik podaje 3 wartości z klawiatury: x, y, z
  wyświetl, któa z tych zmiennych będzie największa
  wykorzystaj instrukcję warunkową
'''

if x >= y and x >= z:
  print(f'Wartość: {x} jest największa')
elif and y >= z:
  print(f'Wartość: {y} jest największa')
else:
  print(f'Wartość: {z} jest największa')

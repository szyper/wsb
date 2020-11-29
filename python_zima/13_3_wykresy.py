import matplotlib.pyplot as plt

plt.bar([1, 2, 3, 4, 5], [5, 2, 7, 8, 2], label='czerwony', color='r')
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label = 'zielony', color = 'g')
plt.legend()
plt.xlabel('Oś X')
plt.ylabel('Oś Y')

plt.title('Wykres\nsłupkowy')
plt.show()

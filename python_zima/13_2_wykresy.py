import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label = "Pierwsza linia")
plt.plot(x2, y2, label = "Druga linia")

plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.title("Graf \n numer 1")
plt.legend()
plt.show()

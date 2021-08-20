import random as r
import matplotlib.pyplot as plt

print(r.randint(1, 20))

print(r.randrange(10, 100, 2))

#reacomodar una lista al azar
lista = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10]
print("Lista original", lista)

r.shuffle(lista)
print("Lista mixeada", lista)

#grafica de campana de gauss
campana = [r.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()


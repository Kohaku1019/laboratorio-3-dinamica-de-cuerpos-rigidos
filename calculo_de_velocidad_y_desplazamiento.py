import matplotlib.pyplot as plt

# Datos
t = 0
distancia = []
velocidad = []
tiempo = []
#lo cual nos permite hallar los datos del desplazamieno del eje y la velocidad angular que posee en cada tiempo
# el cual solo funciona para nuestros datos del pendulo
while t <= 1.055:
    ang = float((14.331 * t * t) + t + 14.122)
    vel = float((28.662 * t) + 1)
    tiempo.append(t)
    distancia.append(ang)
    velocidad.append(vel)
    t += 0.001

# Gráficos
plt.figure(figsize=(10, 5))

# Gráfico de distancia vs tiempo
plt.subplot(2, 1, 1)
plt.plot(tiempo, distancia, color='blue')
plt.title('recorrido')
plt.xlabel('Tiempo [seg]')
plt.ylabel('Distancia [grados°]')

# Gráfico de velocidad vs tiempo
plt.subplot(2, 1, 2)
plt.plot(tiempo, velocidad, color='red')
plt.title('Velocidad angular')
plt.xlabel('Tiempo [seg]')
plt.ylabel('Velocidad [grados°/seg]')

plt.tight_layout()
plt.show()

#imprimir tu nombre
#nombre = input("Introduce tu nombre:")
#print(f"Hola Mundo {nombre} ")
#print("Hola, {}".format(nombre))

#entero
edad = 25

#double
altura = 1.75

#convertir a string
edadString = str(edad)

print(edad + edad)
print(edad + edadString)

print(type(edadString))

tuEdad = input("Introduce tu edad: ")
tuEdad = int(tuEdad)

#estructura de control for
if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
elif tuEdad >= 100:
    print("¿Eres inmortal?")
elif tuEdad <= 0:
    print("No existes")
else:
    print("Eres menor de edad")

#estructura de control for
for i in range(0, 10):
    print(i)

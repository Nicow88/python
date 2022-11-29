import random

salir = 0
nombres = []

        
nombres = []
cantidad = int(input("Cuantos hijos hay que bañar?: "))

for x in range(cantidad):
        item = input('Ingrese un nombre: ')
        nombres.append(item)


aleatorio = random.choice(nombres)
print("Hoy:", aleatorio, "se baña primero!")
input("Presione ENTER para salir")
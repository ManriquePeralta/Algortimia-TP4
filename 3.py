temp = int(input("Ingrese la temperatura: "))
menor = temp
mayor = temp

while temp != 0:
    if temp < menor:
        menor = temp
    if temp > mayor:
        mayor = temp
    temp = int(input("Ingrese un número (-1 para finalizar): "))

print("El menor valor ingresado fue:", menor)
print("El mayor valor ingresado fue:", mayor)

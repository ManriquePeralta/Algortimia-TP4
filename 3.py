num = int(input("Ingrese un número (-1 para finalizar): "))
menor = num
mayor = num

while num != -1:
    if num < menor:
        menor = num
    if num > mayor:
        mayor = num
    num = int(input("Ingrese un número (-1 para finalizar): "))

print("El menor valor ingresado fue:", menor)
print("El mayor valor ingresado fue:", mayor)

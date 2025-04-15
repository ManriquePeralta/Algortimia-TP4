suma = 0
contador = 0
num = 0

print("Ingrese números:")

while suma <= 100:
    num = int(input())
    contador = contador + 1
    if num % 2 == 0:
        suma = suma + num

print("Cantidad total de números ingresados:", contador)

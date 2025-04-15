i = 0
mayor = 0
pos_mayor = 0
suma = 0

print("Ingrese 10 números:")

while i < 10:
    num = int(input())
    suma = suma + num
    if mayor == 0 or num > mayor:
        mayor = num
        pos_mayor = i + 1
    i = i + 1

promedio = suma / 10

print("Promedio de los números ingresados:", promedio)
print("Mayor valor ingresado:", mayor)
print("Primera posición del mayor valor:", pos_mayor)

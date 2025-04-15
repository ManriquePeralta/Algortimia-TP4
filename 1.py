print("Ejercicio 1")
num = int(input("Ingrese un número (-1 para terminar):"))
primero = num
ultimo = num

while num != -1:
    ultimo = num
    num = int(input("Ingrese un número (-1 para terminar):"))

print("Primero:", primero)
print("Último:", ultimo) 





num = int(input("Ingrese un número (-1 para terminar):"))
par = 0

while num != -1:
    if par == 0:
        par = 1
    else:
        par = 0
    num = int(input("Ingrese un número (-1 para terminar):"))

if par == 0:
    print("Cantidad par")
else:
    print("Cantidad impar")


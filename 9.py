num = int(input("Ingrese la terminación de patente entre 0 y 9 (-1 para finalizar): "))
while num < 0 or num > 9:
    print("Número inválido")
    num = int(input("Ingrese la terminación de patente entre 0 y 9 (-1 para finalizar): "))
pares = 0
impares = 0

while num != -1 and num >= 0 and num <= 9:
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    num = int(input("Ingrese la terminación de patente (-1 para finalizar): "))

print("Vehículos con numeración par:", pares)
print("Vehículos con numeración impar:", impares)

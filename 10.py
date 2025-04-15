n = int(input("Ingrese un número mayor o igual a 0: "))

if n < 0:
    print("Número inválido.")
else:
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    print("El factorial de", n, "es:", f)

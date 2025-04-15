num = int(input("Ingrese un número natural para verificar si es primo: "))
i = 2
es_primo = True

if num <= 1:
    es_primo = False
else:
    while i < num:
        if num % i == 0:
            es_primo = False
        i = i + 1

if es_primo:
    print(num, "es un número primo.")
else:
    print(num, "NO es un número primo.")

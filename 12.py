num_terminos = int(input("Ingrese cuántos términos de Fibonacci quiere ver: "))
primer_termino = 0
segundo_termino = 1
suma_total = 0
contador = 0

print("Sucesión de Fibonacci:")

while contador < num_terminos:
    print(primer_termino)
    suma_total = suma_total + primer_termino
    sumatemp = primer_termino
    primer_termino = segundo_termino
    segundo_termino = sumatemp + segundo_termino
    contador = contador + 1

print("Suma de los", num_terminos, "primeros términos:", suma_total)

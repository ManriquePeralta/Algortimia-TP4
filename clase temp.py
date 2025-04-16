"""Se ingresan temperaturas, para realizar la carga se consulta
al usuario si desea ingresar temperaturas, la respuesta es
S o N.
Informar
1) Temperatura maxima, y posicion respecto del ingreso
2) Temperatura minima
3) Porcentaje de temperaturas menores a cero.
4) Promedio de las temperaturas positivas"""

respuesta = input("¿Desea ingresar temperaturas? (S/N): ").upper()

if respuesta != "S":
    print("No se ingresaron temperaturas.")
    exit()

num = int(input("Ingrese una temperatura (0 para finalizar): "))

menor = num

mayor = num
pos_mayor = 1
posicion = 1

contador = 0
contador_negativas = 0

suma_positivas = 0
contador_positivas = 0

while num != 0:
    # Actualizo el valor mas bajo en cada input
    if num < menor:
        menor = num

    # Actualizo el valor mas alto en cada input nuevo y su posición
    if num > mayor:
        mayor = num
        pos_mayor = posicion

    # Contamos temperaturas menores a cero
    if num < 0:
        contador_negativas += 1

    # Sumar temperaturas positivas y contarlas
    if num > 0:
        contador_positivas += 1
        suma_positivas += num #Para luego poder calcular el promedio

    # En cada iteracion incremento el contador total y la posición para cada input
    contador += 1
    posicion += 1

    # Pedimos la nueva temperatura para tener un num actualizado y rehacer todo el proceso del bucle
    num = int(input("Ingrese una temperatura (0 para finalizar): "))

# Calcular el porcentaje de temperaturas menores a cero
if contador > 0:
    porcentaje_negativas = (contador_negativas / contador) * 100
else:
    porcentaje_negativas = 0

# Calcular el promedio de temperaturas positivas
if contador_positivas > 0:
    promedio_positivas = suma_positivas / contador_positivas
else:
    promedio_positivas = 0

# Mostrar los resultados
print("El mayor valor ingresado fue:", mayor, "en la posición:", pos_mayor)
print("El menor valor ingresado fue:", menor)
print("El porcentaje de temperaturas menores a cero es:", porcentaje_negativas, "%")
print("El promedio de las temperaturas positivas es:", promedio_positivas)
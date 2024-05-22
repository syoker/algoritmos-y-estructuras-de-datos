import random

# Definir la semilla del generador de números aleatorios
random.seed(49)

# Generar la lista de 20000 números aleatorios entre 1 y 45000
numeros_aleatorios = [random.randint(1, 45000) for _ in range(20000)]

# Calcular la suma de todos los números generados
suma_total = sum(numeros_aleatorios)

# Verificar la suma correcta para control
if suma_total == 451459554:
    print("Suma correcta de los números generados.")
else:
    print("Error en la generación de números. La suma no coincide.")

# Contadores para múltiplos de 5, 7 y 9
multiplos_5 = 0
multiplos_7 = 0
multiplos_9 = 0

# Mayor número con último dígito entre 5 y 8
mayor_ultimo_digito_5_8 = 0

# Contador de pares menores a 15000
pares_menores_15000 = 0

# Analizar cada número de la lista
for numero in numeros_aleatorios:
    # Múltiplos de 5
    if numero % 5 == 0:
        multiplos_5 += 1

    # Múltiplos de 7
    if numero % 7 == 0:
        multiplos_7 += 1

    # Múltiplos de 9
    if numero % 9 == 0:
        multiplos_9 += 1

    # Mayor número con último dígito entre 5 y 8
    ultimo_digito = numero % 10
    if 5 <= ultimo_digito <= 8 and numero > mayor_ultimo_digito_5_8:
        mayor_ultimo_digito_5_8 = numero

    # Pares menores a 15000
    if numero % 2 == 0 and numero < 15000:
        pares_menores_15000 += 1

# Mostrar resultados
print(f"Múltiplos de 5: {multiplos_5}")
print(f"Múltiplos de 7: {multiplos_7}")
print(f"Múltiplos de 9: {multiplos_9}")
print(f"Mayor número con último dígito entre 5 y 8: {mayor_ultimo_digito_5_8}")

# Porcentaje de pares menores a 15000
porcentaje_pares_menores_15000 = (pares_menores_15000 * 100) // len(numeros_aleatorios)
print(f"Porcentaje de pares menores a 15000: {porcentaje_pares_menores_15000}%")
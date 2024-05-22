import random

random.seed(49)

suma = 0
cont = 0
acum_multi5 = 0
acum_multi7 = 0
acum_multi9 = 0
may58 = None
cont_par15000 = 0

for _ in range(20000):
    cont += 1
    random_number = random.randint(1, 45000)
    suma += random_number
    if (random_number%5) == 0:
        acum_multi5 += 1

    if (random_number%7) == 0:
        acum_multi7 += 1

    if (random_number%9) == 0:
        acum_multi9 += 1

    if 5 <= (random_number % 10) <= 8:
        if may58 is None:
            may58 = random_number
        elif may58 > random_number:
            may58 = random_number

    if (random_number%2) == 0 and random_number < 15000:
        cont_par15000 += 1

def main():
    print('suma:', suma)
    print('multiplos de 5:', acum_multi5)
    print('multiplos de 7:', acum_multi7)
    print('multiplos de 9:', acum_multi9)
    print('numero mayor:', may58)
    print('pares menores de 15000:', cont_par15000)
    print('porcentaje:', cont_par15000*100 // cont) 

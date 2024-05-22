import random
random.seed(20220512)

suma = 0
cont = 0
cont_mult3 = 0
cont_mult5 = 0
cont_mult35 = 0
may = None
cont_par11 = 0
acum_par11 = 0

for _ in range(25000):
    random_number = random.randint(1, 45000)
    suma += random_number
    cont += 1

    if random_number % 3 == 0:
        cont_mult3 += 1
    elif random_number % 5 == 0:
        cont_mult5 += 1
    else:
        cont_mult35 += 1

    if str(random_number)[0] == '1':
        if may is None:
            may = random_number
        elif random_number > may:
            may = random_number

    if random_number % 2 == 0 and random_number % 11 == 0:
        cont_par11 += 1
        acum_par11 += random_number

def main():
    print('suma total:', suma)
    print('cantidad multiplos de 3:', cont_mult3)
    print('cantidad multiplos de 5:', cont_mult5)
    print('cantidad no multiplos de 3 y 5:', cont_mult35)
    print('mayor de los que empiezan con 1:', may)
    print('cont_par11:', cont_par11)
    print('acum_par11:', acum_par11)
    print('promedio:', acum_par11 // cont_par11)
    print('porcentaje cont1:', cont_mult3*100 // cont)
    print('porcentaje cont2:', cont_mult5*100 // cont)
    print('porcentaje cont3:', cont_mult35*100 // cont)

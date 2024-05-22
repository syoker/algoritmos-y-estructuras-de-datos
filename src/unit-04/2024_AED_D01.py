def human_first_part():
    segundos = int(input("Ingrese la cantidad de segundos que pasaron desde la finalización del evento: "))

    minutos = segundos // 60
    horas = minutos // 60

    if horas <= 24:
        print("El tiempo transcurrido fue de", horas, "horas,", minutos % 60, "minutos y", segundos % 60, "segundos")
    else:
        print("Excedido")

def human_second_part():
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    segundos += (minutos * 60) + ((horas * 60) * 60)

    print("La cantidad total de segundos es:", segundos)

def main():
    print('01. Parsear segundos a fecha')
    print('02. Parsear fecha a segundos')
    print('')
    option_selected = input('Selecciona una opcion: ')

    if option_selected in ['01', '1']:
        human_first_part()
    elif option_selected in ['02', '2']:
        human_second_part()
    else:
        print('Opcion inexistente')
            
        
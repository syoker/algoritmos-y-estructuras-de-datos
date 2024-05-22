def convertir_a_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

def main():
    horas = int(input("Ingrese la cantidad de horas: "))
    minutos = int(input("Ingrese la cantidad de minutos: "))
    segundos = int(input("Ingrese la cantidad de segundos: "))
    total_segundos = convertir_a_segundos(horas, minutos, segundos)
    print(f"La cantidad total de segundos es {total_segundos}.")

if __name__ == "__main__":
    main()

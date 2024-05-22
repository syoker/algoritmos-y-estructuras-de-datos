def convertir_segundos(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_restantes_final = segundos_restantes % 60
    return horas, minutos, segundos_restantes_final

def main():
    for _ in range(4):
        segundos = int(input("Ingrese la cantidad de segundos: "))
        horas, minutos, segundos_restantes_final = convertir_segundos(segundos)

        if horas <= 24:
            print(f"El tiempo transcurrido fue de {horas} horas, {minutos} minutos y {segundos_restantes_final} segundos.")
        else:
            print("Excedido")

if __name__ == "__main__":
    main()  
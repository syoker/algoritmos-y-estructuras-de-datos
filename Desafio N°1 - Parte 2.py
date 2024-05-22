horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

segundos += (minutos * 60) + ((horas * 60) * 60)

print("La cantidad total de segundos es:", segundos)
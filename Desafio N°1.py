#Parte 1
segundos = int(input("Ingrese la cantidad de segundos que pasaron desde la finalización del evento: "))

minutos = segundos // 60
horas = minutos // 60

if horas <= 24:
  print("El tiempo transcurrido fue de", horas, "horas,", minutos % 60, "minutos y", segundos % 60, "segundos")
else:
  print("Excedido")

#Parte 2
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

segundos += (minutos * 60) + ((horas * 60) * 60)

print("La cantidad total de segundos es:", segundos)
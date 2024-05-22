segundos = int(input("Ingrese la cantidad de segundos que pasaron desde la finalización del evento: "))

minutos = segundos // 60
horas = minutos // 60

if horas <= 24:
  print("El tiempo transcurrido fue de", horas, "horas,", minutos % 60, "minutos y", segundos % 60, "segundos")
else:
  print("Excedido")
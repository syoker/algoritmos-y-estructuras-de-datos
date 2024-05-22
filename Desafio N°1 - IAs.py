#Parte 1 - ChatGPT
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

#Parte 1 - Gemini
def convertir_segundos(segundos):
  """
  Convierte una cantidad de segundos a horas, minutos y segundos.

  Args:
    segundos: La cantidad de segundos a convertir.

  Returns:
    Una tupla que contiene las horas, minutos y segundos convertidos.
  """
  horas = segundos // 3600
  minutos = (segundos % 3600) // 60
  segundos_restantes = segundos % 60

  return horas, minutos, segundos_restantes

def main():
  """Función principal del programa."""
  while True:
    try:
      segundos_ingresados = int(input("Ingrese la cantidad de segundos: "))
      if segundos_ingresados < 0:
        raise ValueError("La cantidad de segundos no puede ser negativa.")
      horas, minutos, segundos_restantes = convertir_segundos(segundos_ingresados)

      if horas <= 24:
        print(f"Han transcurrido {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
      else:
        print("Excedido")

      break
    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()

#Parte 2 - ChatGPT
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

#Parte 2 - Gemini
def convertir_a_segundos(horas, minutos, segundos):
  """
  Convierte horas, minutos y segundos a una cantidad total de segundos.

  Args:
    horas: La cantidad de horas.
    minutos: La cantidad de minutos.
    segundos: La cantidad de segundos.

  Returns:
    La cantidad total de segundos.
  """
  segundos_totales = (horas * 3600) + (minutos * 60) + segundos
  return segundos_totales

def main():
  """Función principal del programa."""
  while True:
    try:
      horas = int(input("Ingrese la cantidad de horas: "))
      minutos = int(input("Ingrese la cantidad de minutos: "))
      segundos = int(input("Ingrese la cantidad de segundos: "))

      if horas < 0 or minutos < 0 or segundos < 0:
        raise ValueError("Las cantidades de tiempo no pueden ser negativas.")
      segundos_totales = convertir_a_segundos(horas, minutos, segundos)

      print(f"La cantidad total de segundos es {segundos_totales}.")
      break
    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()

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

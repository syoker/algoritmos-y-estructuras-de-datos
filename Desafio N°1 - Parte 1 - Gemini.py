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

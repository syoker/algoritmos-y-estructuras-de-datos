# Código inicial del programa
cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío: "))
pago = int(input("Forma de pago: "))

# Pasamos todas las letras a mayúsculas para evitar problemas
cp = cp.upper()

# Aquí guardamos el recargo basándose en donde se envia el paquete
envio_internacional = 0

# Aquí guardamos en una variable la longitud de código postal ingresado
# para saber de qué país es
longitud_cp = len(cp)

# Aquí definimos la variable "provincia", para que valga "No aplica"
# siempre y cuando no sea una provincia Argentina
provincia = "No aplica"

# Comprobamos si es de Argentina el pedido
if longitud_cp == 8 and cp[0].isalpha() and cp[0] not in "IO" and \
      cp[1:4].isdigit() and cp[5:7].isalpha():
    destino = "Argentina"
    envio_internacional = 0
    if cp[0] == "A":
        provincia = "Salta"
    elif cp[0] == "B":
        provincia = "Provincia de Buenos Aires"
    elif cp[0] == "C":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif cp[0] == "D":
        provincia = "San Luis"
    elif cp[0] == "E":
        provincia = "Entre Ríos"
    elif cp[0] == "F":
        provincia = "La Rioja"
    elif cp[0] == "G":
        provincia = "Santiago del Estero"
    elif cp[0] == "H":
        provincia = "Chaco"
    elif cp[0] == "J":
        provincia = "San Juan"
    elif cp[0] == "K":
        provincia = "Catamarca"
    elif cp[0] == "L":
        provincia = "La Pampa"
    elif cp[0] == "M":
        provincia = "Mendoza"
    elif cp[0] == "N":
        provincia = "Misiones"
    elif cp[0] == "P":
        provincia = "Formosa"
    elif cp[0] == "Q":
        provincia = "Neuquén"
    elif cp[0] == "R":
        provincia = "Río Negro"
    elif cp[0] == "S":
        provincia = "Santa Fe"
    elif cp[0] == "T":
        provincia = "Tucumán"
    elif cp[0] == "U":
        provincia = "Chubut"
    elif cp[0] == "V":
        provincia = "Tierra del Fuego"
    elif cp[0] == "W":
        provincia = "Corrientes"
    elif cp[0] == "X":
        provincia = "Córdoba"
    elif cp[0] == "Y":
        provincia = "Jujuy"
    elif cp[0] == "Z":
        provincia = "Santa Cruz"

# Comprobamos si es de Bolivia el pedido
elif longitud_cp == 4 and cp[0:3].isdigit():
    destino = "Bolivia"
    envio_internacional = 20

# Comprobamos si es de Uruguay el pedido y si es o no de Montevideo
elif longitud_cp == 5 and cp[0:4].isdigit():
    destino = "Uruguay"
    if int(cp[0]) == 1:
        envio_internacional = 20
    else:
        envio_internacional = 25

# Comprobamos si es de Paraguay el pedido
elif longitud_cp == 6 and cp[0:5].isdigit():
    destino = "Paraguay"
    envio_internacional = 20

# Comprobamos si es de Chile el pedido
elif longitud_cp == 7 and cp[0:6].isdigit():
    destino = "Chile"
    envio_internacional = 25

# Comprobamos si es de Brasil el pedido y en que region
elif longitud_cp == 9 and cp[0:4].isdigit() and cp[5] == "-" and \
    cp[6:8].isdigit():
    destino = "Brasil"
    if int(cp[0]) in [8, 9]:
        envio_internacional = 20
    elif int(cp[0]) in [0, 1, 2, 3]:
        envio_internacional = 25
    elif int(cp[0]) in [4, 5, 6, 7]:
        envio_internacional = 30

else:
    destino = "Otro"
    envio_internacional = 50

# Election del tipo de envio elegido por el cliente
precio_envio = 0
if tipo == 0:
    precio_envio = 1100
elif tipo == 1:
    precio_envio = 1800
elif tipo == 2:
    precio_envio = 2450
elif tipo == 3:
    precio_envio = 8300
elif tipo == 4:
    precio_envio = 10900
elif tipo == 5:
    precio_envio = 14300
elif tipo == 6:
    precio_envio = 17900

inicial = (precio_envio/100) * (100 + envio_internacional)

# Descuento del 10%
if pago == 1:
    final = (inicial/10) * 9
else:
    final = inicial

def main():
    print("País de destino del envío:", destino)
    print("Provincia destino:", provincia)
    print("Importe inicial a pagar:", int(inicial))
    print("Importe final a pagar:", int(final))

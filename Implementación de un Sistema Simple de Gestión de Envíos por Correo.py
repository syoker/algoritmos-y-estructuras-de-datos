
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
if longitud_cp == 8 and cp[0] in "ABCDEFGHJKLMNPQRSTUVWXYZ":
    destino = "Argentina"
    envio_internacional = 0
    prov_arg = cp[0]
    if prov_arg == "A":
        provincia = "Salta"
    elif prov_arg == "B":
        provincia = "Provincia de Buenos Aires"
    elif prov_arg == "C":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif prov_arg == "D":
        provincia = "San Luis"
    elif prov_arg == "E":
        provincia = "Entre Ríos"
    elif prov_arg == "F":
        provincia = "La Rioja"
    elif prov_arg == "G":
        provincia = "Santiago del Estero"
    elif prov_arg == "H":
        provincia = "Chaco"
    elif prov_arg == "J":
        provincia = "San Juan"
    elif prov_arg == "K":
        provincia = "Catamarca"
    elif prov_arg == "L":
        provincia = "La Pampa"
    elif prov_arg == "M":
        provincia = "Mendoza"
    elif prov_arg == "N":
        provincia = "Misiones"
    elif prov_arg == "P":
        provincia = "Formosa"
    elif prov_arg == "Q":
        provincia = "Neuquén"
    elif prov_arg == "R":
        provincia = "Río Negro"
    elif prov_arg == "S":
        provincia = "Santa Fe"
    elif prov_arg == "T":
        provincia = "Tucumán"
    elif prov_arg == "U":
        provincia = "Chubut"
    elif prov_arg == "V":
        provincia = "Tierra del Fuego"
    elif prov_arg == "W":
        provincia = "Corrientes"
    elif prov_arg == "X":
        provincia = "Córdoba"
    elif prov_arg == "Y":
        provincia = "Jujuy"
    elif prov_arg == "Z":
        provincia = "Santa Cruz"
    else:
        destino = "Otro"
        provincia = "No aplica"
        envio_internacional = 50

# Comprobamos si es de Bolivia el pedido
elif longitud_cp == 4:
    destino = "Bolivia"
    envio_internacional = 20

# Comprobamos si es de Uruguay el pedido y si es o no de Montevideo
elif longitud_cp == 5:
    destino = "Uruguay"
    if int(cp[0]) == 1:
        envio_internacional = 20
    else:
        envio_internacional = 25

# Comprobamos si es de Paraguay el pedido
elif longitud_cp == 6:
    destino = "Paraguay"
    envio_internacional = 20

# Comprobamos si es de Chile el pedido
elif longitud_cp == 7:
    destino = "Chile"
    envio_internacional = 25

# Comprobamos si es de Brasil el pedido y en que region
elif longitud_cp == 9 and cp[5] == "-":
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

inicial = int(precio_envio/100 * (100 + envio_internacional))

# Descuento del 10%
if pago == 1:
    final = int(inicial/10*9)
else:
    final = inicial


print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)

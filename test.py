cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío: "))
pago = int(input("Forma de pago: "))

cp = cp.upper()
envio_internacional = 0
longitud_cp = len(cp)
provincia = "No aplica"

if longitud_cp == 8 and cp[0] in "ABCDEFGHJKLMNPQRSTUVWXYZ":
    destino = "Argentina"
    envio_internacional = 0
    prov_arg = cp[0]
    provincias = {
        "A": "Salta",
        "B": "Provincia de Buenos Aires",
        "C": "Ciudad Autónoma de Buenos Aires",
        "D": "San Luis",
        "E": "Entre Ríos",
        "F": "La Rioja",
        "G": "Santiago del Estero",
        "H": "Chaco",
        "J": "San Juan",
        "K": "Catamarca",
        "L": "La Pampa",
        "M": "Mendoza",
        "N": "Misiones",
        "P": "Formosa",
        "Q": "Neuquén",
        "R": "Río Negro",
        "S": "Santa Fe",
        "T": "Tucumán",
        "U": "Chubut",
        "V": "Tierra del Fuego",
        "W": "Corrientes",
        "X": "Córdoba",
        "Y": "Jujuy",
        "Z": "Santa Cruz"
    }
    provincia = provincias.get(prov_arg, "No aplica")
    if provincia == "No aplica":
        destino = "Otro"
        envio_internacional = 50

elif longitud_cp == 4:
    destino = "Bolivia"
    envio_internacional = 20

elif longitud_cp == 5:
    destino = "Uruguay"
    if int(cp[0]) == 1:
        envio_internacional = 20
    else:
        envio_internacional = 25
        
elif longitud_cp == 6:
    destino = "Paraguay"
    envio_internacional = 20

elif longitud_cp == 7:
    destino = "Chile"
    envio_internacional = 25

elif longitud_cp == 9 and cp[5] == "-":
    destino = "Brasil"
    if int(cp[0]) == (8 or 9):
        envio_internacional = 20
    elif int(cp[0]) == (0 or 1 or 2 or 3):
        envio_internacional = 25
    elif int(cp[0]) == (4 or 5 or 6 or 7):
        envio_internacional = 30
    else:
        destino = "Otro"
        envio_internacional = 50

else:
    destino = "Otro"
    envio_internacional = 50
    
precio_envio = {
    0: 1100,
    1: 1800,
    2: 2450,
    3: 8300,
    4: 10900,
    5: 14300,
    6: 17900
}.get(tipo, 0)

inicial = int(precio_envio / 100 * (100 + envio_internacional))

if pago == 1:
    final = int(inicial * 0.9)
else:
    final = inicial

print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)

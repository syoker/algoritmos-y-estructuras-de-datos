def mayor_menor(num1, num2):
    if num1 > num2:
        may = num1
        men = num2
    else:
        may = num2
        men = num1
    return may, men

def calculos(may, men):
    cuad = men ** 2
    cubo = may ** 3
    return cuad, cubo

def main():
    num1 = int(input("Ingrese un numero:"))
    num2 = int(input("Ingrese otro numero:"))
    
    may, men = mayor_menor(num1, num2)
    cuad, cubo = calculos(may, men)
    
    print("El menor al cuadrado es:", cuad)
    print("El mayor al cubo es:", cubo)

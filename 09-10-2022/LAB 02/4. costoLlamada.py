# hacer un algoritmo que imprima el costo de una llamada 
# telefónica, capturando la duración de la llamada en minutos y conociendo lo siguiente:
# • Toda llamada que dure tres minutos o menos tiene un costo de $200.
# • Cada minuto adicional cuesta $30.

# importacion de modulos

from datetime import date

# declaracion de variables

duracion = 0
duracionAdicional = 3
PRECIO_REGULAR = 600
PRECIO_ADICIONAL = 90
costoAdicional = 0
total = 0
today = date.today()

# print("")
print(f"\nQuerido usuario, bienvenido al sistema de llamadas.\n(Precios a día {today})" + f"\nCosto regular (hasta los 3 minutos de llamada) = ${PRECIO_REGULAR}\nCosto por cada minuto adicional = ${PRECIO_ADICIONAL}\n")
# print("")

while True:

    print("Por favor, ingrese cuantos minutos duro su llamada:")
    duracion = int(input())
    if duracion == 3:
        total = PRECIO_REGULAR

    if duracion > 3:
        while duracionAdicional < duracion:
            duracionAdicional = duracionAdicional + 1        
    costoAdicional = (duracionAdicional - 3) * PRECIO_ADICIONAL
    total = PRECIO_REGULAR + costoAdicional
    
    print(f"\nCostos a pagar:\nDuracion = {duracion} minutos\nTotal = ${total}")
    print("\nDeseas realizar otra llamada? (S/N):")
    letraPulsada = input()
    
    if letraPulsada == 'N' or letraPulsada == 'n': 
        print("Hasta luego usuario.\n")
        break
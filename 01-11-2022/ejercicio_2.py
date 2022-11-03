# • Para líneas de crédito de Educación, Viajes de vacaciones y _Calamidad domestica
#   se presta un máximo de DOS veces al valor del ahorro del socio.
# • Para la Línea de vehículo se presta un máximo de CUATRO veces el valor del
#   ahorro del socio.
# • Para la línea de vivienda se presta un máximo de SEIS veces el valor del ahorro
#   del socio.

import msvcrt

print("\n     *** Menu Principal ***      ");
print("Bienvenido a la cooperativa de ahorro y credito.\nAqui presentamos nuestras lineas de credito:\n\n1. Educacion\n2. Vacaciones\n3. Vehiculo\n4. Vivienda\n5. Calamidad\n");

while True:
    try:
        opcion = int(input("Ingresa una de las opciones: "));
    except ValueError:
        print("Querido usuario, no ha ingresado ninguna de las opciones validas.");
        continue;
    if opcion < 1 or opcion > 5:
        print("Querido usuario, la opcion ingresada no existe.");
        continue;
    else:
        break;
    
if opcion == 1:
    print("\nPara la linea de credito de educacion, se presta un maximo de dos veces el valor de ahorro del socio.");
    while True:
        try:
            vAhorro = int(input("\nIngresa el valor a depositar como ahorro: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if vAhorro < 0:
            print("\nQuerido usuario, debe ingresar un numero positivo.");
            continue;
        else:
            break;

    while True:
        try:
            potenciador = int(input("\nCuantas veces deseas que se multiplique el ahorro? (Maximo 2)\n: "));
        except ValueError:
            print("\n\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if potenciador < 1 or potenciador > 2:
            print("\nQuerido usuario, debe ingresar un numero entre 1 y 2.");
            continue;
        else:
            break;
    vDevenido = vAhorro * potenciador;
    print(f"\nEl valor ahorrado fue ${vAhorro} COP y el credito entregado al socio fue de ${vDevenido} COP");
if opcion == 2:
    print("\nPara la linea de credito de vacaciones, se presta un maximo de dos veces el valor de ahorro del socio.");
    while True:
        try:
            vAhorro = int(input("\nIngresa el valor a depositar como ahorro: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if vAhorro < 0:
            print("\nQuerido usuario, debe ingresar un numero positivo.");
            continue;
        else:
            break;

    while True:
        try:
            potenciador = int(input("\nCuantas veces deseas que se multiplique el ahorro? (Maximo 2)\n: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if potenciador < 1 or potenciador > 2:
            print("\nQuerido usuario, debe ingresar un numero entre 1 y 2.");
            continue;
        else:
            break;
    vDevenido = vAhorro * potenciador;
    print(f"\nEl valor ahorrado fue ${vAhorro} COP y el credito entregado al socio fue de ${vDevenido} COP");
if opcion == 3:
    print("\nPara la linea de credito de vehiculo, se presta un maximo de cuatro veces el valor de ahorro del socio.");
    while True:
        try:
            vAhorro = int(input("\nIngresa el valor a depositar como ahorro: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if vAhorro < 0:
            print("\nQuerido usuario, debe ingresar un numero positivo.");
            continue;
        else:
            break;

    while True:
        try:
            potenciador = int(input("\nCuantas veces deseas que se multiplique el ahorro? (Maximo 4)\n: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if potenciador < 1 or potenciador > 2:
            print("\nQuerido usuario, debe ingresar un numero entre 1 y 4.");
            continue;
        else:
            break;
    vDevenido = vAhorro * potenciador;
    print(f"\nEl valor ahorrado fue ${vAhorro} COP y el credito entregado al socio fue de ${vDevenido} COP");
if opcion == 4:
    print("\nPara la linea de credito de vivienda, se presta un maximo de seis veces el valor de ahorro del socio.");
    while True:
        try:
            vAhorro = int(input("\nIngresa el valor a depositar como ahorro: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if vAhorro < 0:
            print("\nQuerido usuario, debe ingresar un numero positivo.");
            continue;
        else:
            break;

    while True:
        try:
            potenciador = int(input("\nCuantas veces deseas que se multiplique el ahorro? (Maximo 6)\n: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if potenciador < 1 or potenciador > 6:
            print("\nQuerido usuario, debe ingresar un numero entre 1 y 6.");
            continue;
        else:
            break;
    vDevenido = vAhorro * potenciador;
    print(f"\nEl valor ahorrado fue ${vAhorro} COP y el credito entregado al socio fue de ${vDevenido} COP");
if opcion == 5:
    print("\nPara la linea de credito de calamidad domestica, se presta un maximo de dos veces el valor de ahorro del socio.");
    while True:
        try:
            vAhorro = int(input("\nIngresa el valor a depositar como ahorro: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if vAhorro < 0:
            print("\nQuerido usuario, debe ingresar un numero positivo.");
            continue;
        else:
            break;

    while True:
        try:
            potenciador = int(input("\nCuantas veces deseas que se multiplique el ahorro? (Maximo 2)\n: "));
        except ValueError:
            print("\nQuerido usuario, no ha ingresado una cantidad valida.");
            continue;
        if potenciador < 1 or potenciador > 2:
            print("\nQuerido usuario, debe ingresar un numero entre 1 y 2.");
            continue;
        else:
            break;
    vDevenido = vAhorro * potenciador;
    print(f"\nEl valor ahorrado fue ${vAhorro} COP y el credito entregado al socio fue de ${vDevenido} COP");
    
print(f"\nPresiona cualquier tecla para salir..."), msvcrt.getch()

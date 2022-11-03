import msvcrt

# Declaracion de variables

GANANCIAS_AREAS = ['5%', '10%', '15%'];
i = True;

while True:
    try:
        ganancias = int(input("Ingresar por favor las ganancias de la empresa este año: "));
    except ValueError:
        print("Querido usuario, usted no ingresó un número. Por favor ingrese la cantidad de ganancias totales este año.");
        continue;
    if ganancias < 0:
        print("Querido usuario. Debe ingresar un numero positivo o 0.")
    else:
        break;
    
while True:
    try:
        empleadosAdministrativos = int(input("Ingresar por favor el total de empleados administrativos: "));
    except ValueError:
        print("Querido usuario, usted no ingresó un número. Por favor ingrese la cantidad de empleados administrativos.");
        continue;
    if empleadosAdministrativos < 0:
        print("Querido usuario. Debe ingresar un numero positivo o 0.")
    else:
        break;

while True:
    try:
        empleadosComerciales = int(input("Ingresar por favor el total de empleados comerciales: "));
    except ValueError:
        print("Querido usuario, usted no ingresó un número. Por favor ingrese la cantidad de empleados comerciales.");
        continue;
    if empleadosComerciales < 0:
        print("Querido usuario. Debe ingresar un numero positivo o 0.")
    else:
        break;

while True:
    try:
        empleadosTecnicos = int(input("Ingresar por favor el total de empleados tecnicos: "));
    except ValueError:
        print("Querido usuario, usted no ingresó un número. Por favor ingrese la cantidad de empleados tecnicos.");
        continue;
    if empleadosTecnicos < 0:
        print("Querido usuario. Debe ingresar un numero positivo o 0.")
    else:
        break;

while i == True:
    print(f"\n*** Total de empleados registrados: ***\nÁrea Administrativa: {empleadosAdministrativos}\nÁrea Comercial: {empleadosComerciales}\nÁrea Técnica: {empleadosTecnicos}\n")
   
    #nombre
    nombreEmpleado = input("Ingresa tu nombre completo: ");

    #edad
    while True:
        try:
            edadEmpleado = int(input("Escribe tu edad: "));
        except ValueError:
            print("Querido usuario, usted no ingresó un número. Por favor ingrese su edad correctamente.");
            continue;
        if edadEmpleado < 0:
            print("Querido usuario, debe ingresar un numero positivo. Por favor ingrese su edad correctamente.");
            continue;
        else:
            break;
    
    #genero
    while True:
        try:
            generoEmpleado = int(input("Ingresa tu género: \n1.Masculino\n2.Femenino\n3.Otro\n: "));
        except ValueError:
            print("Querido usuario, esta no es una opción valida. Por favor ingrese el número de alguna de las 3 opciones.");
            continue;
        if generoEmpleado < 1 or generoEmpleado > 3:
            print("Querido usuario, esta no es una opción valida. Por favor ingrese el número de alguna de las 3 opciones.");
            continue;
        else:
            break;
    if generoEmpleado == 1:
        generoEmpleado = "Masculino";
    elif generoEmpleado == 2:
        generoEmpleado = "Femenino";
    elif generoEmpleado == 3:
        generoEmpleado = "Otro";
    
    # areas
    while True:
        try:
            areaEmpleado = int(input("Ingresa tu área de trabajo: \n1.Administrativa\n2.Comercial\n3.Técnica\n: "));
        except ValueError:
            print("Querido usuario, esta no es una opción valida. Por favor ingrese el número de alguna de las 3 opciones.");
            continue;
        if areaEmpleado < 1 or areaEmpleado > 3:
            print("Querido usuario, esta no es una opción valida. Por favor ingrese el número de alguna de las 3 opciones.");
            continue;
        else:
            break;
    if areaEmpleado == 1:
        areaEmpleado = "Administrativa";
        valorDevenido = (ganancias * 10 / 100) / empleadosAdministrativos;
        porcentaje = GANANCIAS_AREAS[1];
    elif areaEmpleado == 2:
        areaEmpleado = "Comercial";
        valorDevenido = (ganancias * 5 / 100) / empleadosComerciales;
        porcentaje = GANANCIAS_AREAS[0];
    elif areaEmpleado == 3:
        areaEmpleado = "Técnica";
        valorDevenido = (ganancias * 15 / 100) / empleadosTecnicos;
        porcentaje = GANANCIAS_AREAS[2];

    # validacion boletas
    boleta = "Empleado no aplica para boletas de algún show";
    
    if edadEmpleado > 30 and areaEmpleado == "Administrativa":
        boleta = "Querido usuario, por favor reclamar la boleta para el show del viernes."
    elif generoEmpleado == "Femenino" and areaEmpleado == "Técnica":
        boleta = "Querido usuario, por favor reclamar la boleta para el show del sábado."


    #impresion de resultados
    print("*"*15);
    print(f"Nombre del empleado: {nombreEmpleado}");
    print(f"Área laboral del empleado: {areaEmpleado}");
    print(f"Valor a recibir: ${valorDevenido} COP como parte del {porcentaje} del total de ganancias de la empresa dividido entre el numero de trabajadores de su area.");
    print(f"{boleta}\n")
    print("*"*15)   

    #valdiar si se quiere agregar otro empleado
    while True:
        try:
            validacionCiclo = int(input("Desea registrar otro empleado?\n1.Si\n2.No\n: "));
        except ValueError:
            print("Querido usuario, esta no es una opción valida. Por favor ingrese el número de alguna de las 2 opciones.");
            continue;
        if validacionCiclo < 1 or validacionCiclo > 2:
            print("Querido usuario, esta no es una opción valida. Por favor ingrese el número de alguna de las 2 opciones.");
            continue;
        else:
            break;
        
    if validacionCiclo == 1:
        continue;
    if validacionCiclo == 2:
        i = False;
    
print(f"\nPresiona cualquier tecla para salir..."), msvcrt.getch()
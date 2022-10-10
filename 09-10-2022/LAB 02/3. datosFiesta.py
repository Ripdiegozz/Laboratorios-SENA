asistentes = 0
edad_mas_joven = 0
hombres = 0
mujeres = 0
promedio_hombres = 0
promedio_mujeres = 0
while True:
    print("Ingresa la edad del asistente:")
    edad = int(input())
    print("Selecciona el valor de genero.")
    print("    1.- Mujer")
    print("    2.- Hombre")
    while True:
        genero = int(input(": "))
        if genero<1 or genero>2:
            print("Valor incorrecto. Ingresalo nuevamente:")
        if genero>=1 and genero<=2: break
    if edad>=18:
        asistentes = asistentes+1
    else:
        print("No se permiten menores de edad a la fiesta.")
    if genero==1 and edad>=18:
        mujeres = mujeres+1
        promedio_mujeres = promedio_mujeres+edad
    if genero==2 and edad>=18:
        hombres = hombres+1
        promedio_hombres = promedio_hombres+edad
    if edad>=18 and (edad_mas_joven==0 or edad_mas_joven>edad):
        edad_mas_joven = edad
    print("")
    while True:
        print("Deseas registrar otro invitado? (S/N):")
        tecla_repetir = input()
        if tecla_repetir=="s" or tecla_repetir=="n" or tecla_repetir=="S" or tecla_repetir=="N": break
    if tecla_repetir=="n" or tecla_repetir=="N": break
if hombres==0:
    promedio_hombres = 0
else:
    promedio_hombres = round(promedio_hombres/hombres,2)
if mujeres==0:
    promedio_mujeres = 0
else:
    promedio_mujeres = round(promedio_mujeres/mujeres, 2)
  
    ## imprimir resultados al usuario 
print("")
print("***************************************************")
print("Numero de asistentes totales:",asistentes)
print("Edad del asistenete mas joven:",edad_mas_joven)
print("Numero de hombres que asistieron:",hombres)
print("Numero de mujeres que asistieron:",mujeres)
print("Edad promedio de los hombres:",promedio_hombres)
print("Edad promedio de las mujeres:",promedio_mujeres)


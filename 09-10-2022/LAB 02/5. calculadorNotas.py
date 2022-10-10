# un grupo de 10 estudiantes presentan un examen de Física. 
# Hacer un algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule 
# e imprima:
# • La cantidad de estudiantes que obtuvieron una calificación menor a 50.
# • La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor 
# que 70.
# • La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor 
# que 80.
# • La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
# La calificación obtenida en el examen de física debe ser entre 1 y 100

print("Por favor, ingresa el numero de alumnos que registraran sus notas:")
n = int(input(': '))
i = 1
estudiantesMenor50 = 0 
estudiantesMas50Menor70 = 0
estudiantesMas70Menor80 = 0
estudiantesMas80 = 0
while i <= n:
    print(f"Ingresa tu nota en el examen, estudiante numero {i}")
    nota = int(input())
    while nota < 1 or nota > 100:
        print("El rango de notas va de 1 a 100, por favor ingrese su nota correctamente:")
        nota = int(input())
    if nota < 50:
        estudiantesMenor50 = estudiantesMenor50 + 1;
    if nota >= 50 and nota < 70:
        estudiantesMas50Menor70 = estudiantesMas50Menor70 + 1;
    if nota >= 70 and nota < 80:
        estudiantesMas70Menor80 = estudiantesMas70Menor80 + 1;
    if nota >= 80:
        estudiantesMas80 = estudiantesMas80 + 1;
    i += 1
        
print("\nResultados:");        
print(f"{estudiantesMenor50} estudiantes sacaron menos de 50 puntos");        
print(f"{estudiantesMas50Menor70} estudiantes sacaron de 50 a 70 puntos");        
print(f"{estudiantesMas70Menor80} estudiantes sacaron de 70 a 80 puntos");        
print(f"{estudiantesMas80} estudiantes sacaron de 80 a 100 puntos");        

        
        

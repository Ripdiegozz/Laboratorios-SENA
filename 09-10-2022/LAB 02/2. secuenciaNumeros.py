# hacer un algoritmo que imprima los primeros 20 términos de 
# la siguiente serie:
#1, 3, 6, 10, 15, 21, 28,……..

indice = 2;
numero = 1;
print("Cual numero quieres que sea el ultimo en sumarse a la serie?");
tope = int(input())

print("Inicio de secuencia:")
print(numero)
while numero <= tope:
    numero = numero + indice;
    print(numero);
    indice += 1;
    
print("Secuencia terminada correctamente!")
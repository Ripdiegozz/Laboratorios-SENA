Algoritmo sumaCifras
	Escribir 'Ingresa un número, mínimo de 4 cifras'
	Leer cantidad
	suma <- 0
	Mientras cantidad>0 Hacer
		digito <- cantidad MOD 10
		suma <- suma+digito
		Escribir digito
		cantidad <- TRUNC(cantidad/10)
	FinMientras
	Escribir 'La suma de cifras es: ',suma
FinAlgoritmo

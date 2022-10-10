Algoritmo funcionMatematica
	i <- i
	suma <- 0
	sumaMultiplos <- 0
	sumaCincos <- 0
	n <- _y MOD 10
	Escribir 'Inicio de secuencia:'
	Mientras i<11 Hacer
		_y <- (i^2)-(2*i)
		Escribir _y
		Si _y<>0 Entonces
			Si _y MOD 3=0 Entonces
				Escribir 'El numero ',_y,' es multiplo de 3'
				sumaMultiplos <- _y+sumaMultiplos
			FinSi
			Si _y MOD 10=5 Entonces
				Escribir 'El ultimo digito del numero ',_y,' es 5'
				Escribir ''
				sumaCincos <- _y+sumaCincos
			FinSi
		FinSi
		suma <- suma+_y
		i <- i+1
	FinMientras
	Escribir ''
	Escribir 'La suma de Y es ',suma
	Escribir 'La suma de todos los multiplos de 3 es ',sumaMultiplos
	Escribir 'La suma de todos los numeros, cuyo ultimo digito es 5 es ',sumaCincos
FinAlgoritmo

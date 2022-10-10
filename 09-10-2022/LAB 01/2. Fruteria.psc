Algoritmo Fruteria
	Escribir 'Ingresa el numero de kilos que llevaras:' Sin Saltar
	Leer numeroKilos
	compra <- 4200.0*numeroKilos
	descuento <- 0
	Si numeroKilos>2 Entonces
		descuento <- compra*0.1
	FinSi
	Si numeroKilos>5 Entonces
		descuento <- compra*0.15
	FinSi
	Si numeroKilos>10 Entonces
		descuento <- compra*0.2
	FinSi
	pago <- compra-descuento
	Escribir 'Total de compra: ',compra
	Escribir 'Total de descuento: ',descuento
	Escribir 'Total a pagar: ',pago
FinAlgoritmo

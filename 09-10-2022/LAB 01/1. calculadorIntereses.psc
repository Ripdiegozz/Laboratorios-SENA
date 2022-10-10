Algoritmo calculadorIntereses
	Escribir 'Ingresa el valor de deposito:' Sin Saltar
	Leer deposito
	interes <- 0.02
	meses <- 12*5
	saldo <- deposito*(1.0+interes)^(meses)
	Escribir 'Total de interes: ',interes
	Escribir 'Numero de meses: ',meses
	Escribir 'Total de saldo: ',TRUNC(saldo)
FinAlgoritmo

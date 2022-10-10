# Desarrollar un algoritmo que calcule el salario neto que debe recibir 
# un vendedor de un almacén. Se debe tener en cuenta si tiene derecho o no al auxilio de 
# transporte.

SMLV = 1000000
AUXILIO_TRANSPORTE = 117172
validador = True
while validador == True:
	
		print("Por favor, ingrese el nombre y apellido del empleado:")
		usuario = input()
		print("Por favor, ingrese el numero de identificaion del empleado",usuario,":")
		idUsuario = input()
		
		print("Por favor, ingresa el numero de dias que el empleado",usuario,"laboro este mes:")
		diasLaborados = int(input())
		while diasLaborados > 30 or diasLaborados < 1:
			print("Atencion, el numero de dias laborados posibles van de 1 a 30. Ingrese correctamente el numero de dias que laboro el empleado")
			diasLaborados = int(input())
		print("Por favor, ingresa la cantidad total de ventas (en pesos) que realizo el empleado",usuario,"este mes: ")
		ventasTotales = float(input())
		print("Por favor, ingrese la cantidad total de prestamos (en pesos) que realizo el empleado",usuario,"este mes ")
		deducciones = float(input())
		# realizar operaciones
  
		salarioDevengado = SMLV*diasLaborados/30
		if salarioDevengado<=(SMLV*2):
			salarioDevengado = salarioDevengado+AUXILIO_TRANSPORTE
		ventasTotales = (ventasTotales*2)/100
		totaldevengado = salarioDevengado+ventasTotales
		salarioneto = int(salarioDevengado-deducciones)
  
		# Imprimir en pantalla los resultados
		print(" ")
		print("Cedula del empleado:", idUsuario)
		print("Nombre del empleado:", usuario)
		print("*Cantidades mostradas en pesos colombianos*")
		print("Salario basico:",SMLV)
		print("Auxilio de transporte:",AUXILIO_TRANSPORTE)
		print("Comision de ventas:", ventasTotales)
		print("Prestamos:", deducciones)
		print("Salario neto a recibir:", salarioneto)
		print(" ")
		print("***********************************************")
		print(" ")
		print("Que deseas hacer a continuacion? (Ingresa el numero de la opcion)")
		print("1. Calcular el salario neto de otro empleado")
		print("2. Salir de la aplicacion")
		validadorUsuario = int(input())
		while validadorUsuario > 2 or validadorUsuario < 1:
			print("Solo existen dos opciones, por favor selecciona una de ellas.")
			validadorUsuario = int(input())
		if validadorUsuario == 2:
			print("Saliendo del programa.")
			validador = False


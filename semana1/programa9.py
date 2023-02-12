def mayor(numero1:int,numero2:int)->int:
	mayor=None
	if numero1>numero2:
		mayor = numero1
	elif numero2>numero1:
		mayor = numero2
	else:
		mayor=None
	return mayor 
print(mayor(3,2))	#3
print(mayor(2,3))	#3
print(mayor(3,3))	#None

while True:
	salir = input ("Quiere comenzar la aventura? (s/n)")
	if salir == "n":
		break
	vidaelfo = 3
	vidaorco = 3	
	while vidaorco > 0 and vidaelfo > 0:	
		ataque = input ("atacar con el elfo (s/n)")
		if ataque == "s":
			vidaorco = vidaorco - 1
			if vidaorco >=2 or vidaorco == 0:
			 print("Atacaste al orco, le quedan", vidaorco, "puntos de vida" )
			else:
				print("Atacaste al orco, le queda", vidaorco, "punto de vida" ) 
		elif ataque == "n":
			vidaelfo = vidaelfo - 1
			if vidaorco >=2 or vidaorco == 0:
				print("El orco te atacó, te quedan", vidaelfo, "puntos de vida" )
			else:
				print("Atacaste al orco, le queda", vidaelfo, "punto de vida" )
	if vidaorco == 0:
		print("Mataste al orco")
	if vidaelfo == 0:
		print("El orco te mató")
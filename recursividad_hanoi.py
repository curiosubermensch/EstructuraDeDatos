def hanoi(n,i,f,a):	
	if n==1:
		print(f"C.B: mover disco {n} desde {i} hasta {f}")
		return
	else:	
		hanoi(n-1,i,a,f)	
		print(f"     mover disco {n} desde {i} hasta {f}")
		hanoi(n-1,a,f,i)
		

def torrehanoi(n,o,a,d): #parte moviendo de o a d
	if n>0:
		torrehanoi(n-1,o,d,a) #movera el disco 2 de o al aux (lo q implica mover el disco 1 dos veces)
		#despues de q termine la anterior llamada recursiva y se alcancen los C.B imprimirá lo sgte
		print(f"mover {n} de {o} a {d}") #recordar q 
		torrehanoi(n-1,a,o,d) #movera el disco 2 del aux al de destino (lo q implica mover el disco 1 dos veces)
#torrehanoi(3,"A","B","C")
# mover 1 de A a C
# mover 2 de A a B
# mover 1 de C a B
# mover 3 de A a C
# mover 1 de B a A
# mover 2 de B a C
# mover 1 de A a C

def hanoi2(n,o,d,a):
	if n==1:
		print(f"mover disco {n} de {o} a {d}")
		return
	else:	
		hanoi2(n-1,o,a,d)	
		print(f"mover disco {n} de {o} a {d}")
		hanoi2(n-1,a,d,o)
hanoi2(3,"A","C","B")
# mover disco 1 de A a C
# mover disco 2 de A a B
# mover disco 1 de C a B
# mover disco 3 de A a C
# mover disco 1 de B a A
# mover disco 2 de B a C
# mover disco 1 de A a C



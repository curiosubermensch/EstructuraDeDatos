#contar desde m hasta n (hacia adelante) con recursion:

def cuenta(m,n):
	if m==n: #CASO BASE
		print(m) #se imprime el ultimo y no se vuelve a llamar más porque no pasa al else 
	else:  #DOMINIO
		print(m)
		cuenta(m+1,n)
		#cuando vuelva a llamarse m=m+1, osea que habrá aumentado el valor de m y dicho valor aumentado sera el que se evaluará en el if


def cuentaSaliendo(x,y):
	if x==y:
		print("CASO BASE ENCONTRADO ",x)
	else:
		print("no hemos encontrado el caso base x = ",x)
		cuentaSaliendo(x+1,y)
		print("saliendo de la recursion: x = ",x) #esto se imprime la misma cantidad de veces que se llamo la funcion y va decrementando x que fue aumentada, la decrementa hasta dejarla en el valor inicial

#cuentaSaliendo(1,3)
cuentaSaliendo(1,4)
"""
no hemos encontrado el caso base x =  1  #cuentaSaliendo(1+1,4) 
no hemos encontrado el caso base x =  2  #cuentaSaliendo(2+1,4) 
no hemos encontrado el caso base x =  3  #cuentaSaliendo(3+1,4) 
CASO BASE ENCONTRADO  4                  #[x = 4]  
#Luego de encontrar el c.base se empieza a evaluar la sentencia q estaba 
#debajo d la llamada d la funcion a sí misma
saliendo de la recursion: x =  3         #cuentaSaliendo(3+1,4) [m valia 3 antes de sumarle 1] 
saliendo de la recursion: x =  2         #cuentaSaliendo(2+1,4) [m valia 2 antes de sumarle 1] 
saliendo de la recursion: x =  1         #cuentaSaliendo(1+1,4) [m valia 1 antes de sumarle 1] 
"""


def bajarEscalera(p):
	if p==0:
		print("la bajaste")
	else:
		print("bajando peldaño: ",p)
		bajarEscalera(p-1)

#bajarEscalera(4)
"""
bajando peldaño:  4
bajando peldaño:  3
bajando peldaño:  2
bajando peldaño:  1
la bajaste
"""


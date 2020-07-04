#funcion que determine si un numero es primo:
import random

def primo(n):
	c=0
	for i in range(1,n+1):
		if n%i==0:
			c+=1
	if c==2:
		print("++++++++++++++++")
		print(n," ES PRIMO")
		print("++++++++++++++++")
	elif c>2:
		print(n, " no es primo")


def primo2(n):
	#no considera ni el 1 ni a si mismo (n no lo toma como rango)
	#asi que si en ese rango hay algun modulo que sea cero es porque no era primo
	for i in range(2,n):
		if n%i==0:
			return False
	return True #tiene que estar a este nivel, cuando termina el for, si pasa todas las vueltas de for es porque era primo, sino retorna que era falso (entro en el if del for)


# for x in range(1,200):
# 	primo(x)
# 	print("################################")

print(primo2(9))



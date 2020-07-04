"""
Definir dos funciones para calcular la suma de 1 a n numeros. 
Una de ellas suma uno a uno cada numero (metodo lento)
la otra aplica la formula de la suma aritmetica de gauss (n+1)(n/2)
"""

import time

def suma_lineal(n):
	suma=0
	for i in range(1,n+1):
		suma+=i
	return suma

def suma_constante_gauss(n):
	return (1+n)*(n/2)

cantidad=1000000 #el valor que le pasaremos a las funciones(?)

for i in range(4):
	t0=time.time() #tiempo inicial
	suma1=suma_lineal(cantidad)
	t1=time.time() #tiempo cuando termina de ejecuarse la suma lineal
	suma2=suma_constante_gauss(cantidad)
	t2=time.time() #tiempo cuando termina de ejecuarse la suma de gauss

	#imprimimos los resultados por pantalla:
	print("suma lineal: ","{} - {}".format(suma1, t1-t0)) #imprimimos el valor de la suma y cuanto tardó
	print("suma gauss : ","{} - {}".format(suma2, t2-t1)) 

	cantidad *=10 #cantidad por vueltas: 1 millon, 10 millones, 100 mill, 1000 mill.

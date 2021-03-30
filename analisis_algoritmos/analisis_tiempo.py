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

def main():
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


def mainDos(): #suma lineal
	cantidad=1000
	for i in range(5):
		t0=time.time()
		s=suma_lineal(cantidad)
		t1=time.time()
		print("La suma es %d y requirió %10.15f segundos" %(s,t1-t0))
		cantidad*=10

mainDos()
# La suma es 500500 y requirió 0.000000000000000 segundos
# La suma es 50005000 y requirió 0.001002788543701 segundos
# La suma es 5000050000 y requirió 0.007003545761108 segundos
# La suma es 500000500000 y requirió 0.106076002120972 segundos
# La suma es 50000005000000 y requirió 0.722471714019775 segundos
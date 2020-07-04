#sucesion de fibonacci recursiva:
#la sucesion parte con 1 y 0, a partir de estos nros cada
#termino sgte es la suma de los dos anteriores
#0,1,1,2,3,,5,8,13,21,34,55,89,144,233,377,610,987,...
#sea n la posicion del numero de fibonacci (partiendo de 0):
def fibonacci(n):
	if n==1 or n==2:
		return 1;
	else:
		return fibonacci(n-1)+fibonacci(n-2)


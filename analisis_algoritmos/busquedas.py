import time

#busqueda lineal:
l=[1,2,4,5,6,74,35,16,7,77]

def busqueda_lineal(lista,n):
	for i in lista:
		if n==i:
			return True
	return False

def busqueda_binaria():
	pass

def main():
	t0=time.time()
	x=busqueda_lineal(l,74)
	t1=time.time()
	print("busqueda lineal: ",x, end="| ")
	print("tiempo: %.16f" %(t0-t1))


main()
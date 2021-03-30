cantidades=[61,52,34,45,36,24,16,4,5,52,43,6,54,65]
n=55

def suma_tres(lista, valor):
	trios=[]
	for i in lista:
		for j in lista:
			for k in lista:
				if i+j+k==valor:
					trios.append([i,j,k])
	return trios

print(suma_tres(cantidades,n))
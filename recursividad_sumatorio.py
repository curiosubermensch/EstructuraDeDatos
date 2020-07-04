#sumatorio se le pasa un numero y suma todos los anteriores con recursividad:

def sumatorio(n):
    if n==0:
        return 0  
    else:
        return n + sumatorio(n-1) #formula general, siempre se debe pensar antes de codificar

#mejorar funcion para que calcule sumatoria de n° negativos:
def sumatorio2(n):
	if n==0:
		return 0
	else:
		if n>=0:
			return n+sumatorio2(n-1)
		else:
			return n+sumatorio2(n+1)



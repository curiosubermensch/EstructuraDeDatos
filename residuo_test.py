#dados dos numeros enteros a>=0 y b>0, calcular el residuo de su division entera a/b
import random

def resto(a,b):
	if a<b:
		return 0 #¿o a?
	else:
		return 1 + resto(a-b,b)

def resto2(x,y):
	if x<y:
		return x
	else:
		return 1 + resto(x-y,y)

# for i in range(100):
# 	m=random.randint(1,500)
# 	n=random.randint(1,500)
# 	print("valor a=",m)
# 	print("valor b=",n)
# 	print("mi codigo --->residuo: ",resto(m,n))
# 	print("codigo video --->residuo: ",resto2(m,n))
# 	print("#####################################################")

#conclusion: mi codigo está malo porque no es cero el residuo cuando el divisor es mas grande que el dividendo, el RESIDUO en ese caso es el DIVIDENTO


def modulo(m,n):
	if m<n:
		print("------caso base encontrao: ",m)
		return m
	else:
		print("valores de a y b: ",m,", ",n)
		return 1+modulo(m-n,n)
print(modulo(17,5))


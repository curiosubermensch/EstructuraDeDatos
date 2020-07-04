def factorial(n):
	if n==0: #cuando acaba 
		return 1 
	else:
		return n*factorial(n-1)

print(factorial(5)) #5*4*3*2*1

"""
Devuelve 5 * factorial (4) entra en primera recursión
factorial (4) devuelve 4 * factorial (3) entra en segunda recursión
factorial (3) devuelve 3 * factorial (2) entra en tercera recursión
factorial (2) devuelve 2 * factorial (1) entra en cuarta recursión
factorial (1) devuelve 1 * factorial (0) entra en quinta recursión
factorial (0) devuelve 1 y termina la quinta recursión que devuelve 1*1

termina la cuarta recursión que devuelve 2*1
termina la tercera recursión que devuelve 3*2*1
termina la segunda recursión que devuelve 4*3*2*1
termina la primera recursión que devuelve 5*4*3*2*1
"""
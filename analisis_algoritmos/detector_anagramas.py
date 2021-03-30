"""
Una cadena es un anagrama de otra si la segunda es simplemente un reordenamiento de la primera. Por ejemplo, 'fresa' y 'frase' son anagramas. Las cadenas 'caro' y 'roca' son también anagramas. Por razones de simplicidad, asumiremos que las dos cadenas en cuestión son de la misma longitud y que están escritas en minúsculas. Nuestro objetivo es escribir una función booleana que tomará dos cadenas y devolverá una confirmación de si son o no anagramas.
"""

#fuerza bruta O(n)
def anagrama(a,b):
	if len(a)==len(b):
		c=0
		for i in a:
			if i in b:
				c+=1
		if len(a)==c:
			return True
		return False
	else:
		print("error de ingreso")


print(anagrama("gate","gato"))
print(anagrama("nacionalista","altisonancia"))
""""
[ 1 ] z = z
[ 2 ] a = a
[ 3 ] a = a
[ 4 ] p = p
[ 5 ] a = a
[ 6 ] a = a
[ 7 ] t = t
[ 8 ] o = o
False
"""


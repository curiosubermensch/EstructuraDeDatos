#https://ibb.co/pRwYRLc
# Si la cadena está hecha de cero letras o de una letra, entonces es un palíndromo.
# De lo contrario, compara la primera y la última letra de la cadena.
# Si la primera y la última letra difieren, entonces la cadena no es un palíndromo.
# De lo contrario, la primera y la última letra son la misma. Elimínalas de la cadena y determina si la cadena que queda es un palíndromo. Toma la respuesta para esta cadena más pequeña y úsala como la respuesta para la cadena original.
#------------------------------------------------------------------------------------------------

def palindromo(c):
	if len(c)==1 or len(c)==0:
		return True
	else:
		if c[0]==c[-1]:
			return palindromo(c[1:-1])
		else:
			return False

c="rotor"
d="xyzax"
print(palindromo(c)) #True
print(palindromo(d)) #False
